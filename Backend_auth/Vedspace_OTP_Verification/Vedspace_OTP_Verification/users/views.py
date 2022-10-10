from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
import json

from .models import (
    UserToken
)

from .mixins import (
    FormErrors,
    RedirectParams,
    TokenGenerator,
    ActivateTwoStep,
    CreateEmail
)

from .forms import (
    UserForm,
    UserProfileForm,
    ForgottenPasswordForm,
    AuthForm,
    RequestPasswordForm,
    TwoStepForm
)

from django.shortcuts import HttpResponse

'''
 is_ajax() deprecated 
'''
# class AjaxMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         def is_ajax(self):
#             return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        
#         request.is_ajax = is_ajax.__get__(request)
#         response = self.get_response(request)
#         return response

# class AjaxResponseMixin(object):
#       def dispatch(self, request, *args, **kwargs):
#         request_method = request.method.lower()
#             if request.is_ajax and request_method in self.http_method_names:



# def is_ajax(request):
#     return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


# def ajax_test(request):
#     if is_ajax(request=request):
#         message = "This is ajax"
#     else:
#         message = "Not ajax"
#     return HttpResponse(message)

'''
Basic view for user sign up
'''


def sign_up(request):
    # redirect if user is already signed in
    if request.user.is_authenticated:
        return redirect(reverse('users:account'))

    u_form = UserForm()
    up_form = UserProfileForm()
    result = "error"
    message = "Something went wrong. Please check and try again"

    # Safe guard to stop sign up until API key is added
    if settings.TWILIO_AUTH_TOKEN == "XXX":
        return HttpResponse(
            json.dumps({"result": result, "message": message}),
            content_type="application/json"
        )

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        u_form = UserForm(data=request.POST)
        up_form = UserProfileForm(data=request.POST)

        # if both forms are valid, do something
        if u_form.is_valid() and up_form.is_valid():
            user = u_form.save()

            # commit = False is used as userprofile.user can not be null
            up = up_form.save(commit=False)
            up.user = user
            up.save()

            # Mark user profile as inactive until verified
            user.is_active = False
            user.email = user.username
            user.save()

            # create a new token
            token = TokenGenerator()
            make_token = token.make_token(user)
            url_safe = urlsafe_base64_encode(force_bytes(user.pk))

            # create and sends a SMS code
            sms_code = ActivateTwoStep(user=user, token=make_token)

            result = "perfect"
            message = "We have sent you an SMS"
            context = {"result": result, "message": message, "url_safe": url_safe, "token": make_token}
        else:
            message = FormErrors(u_form, up_form)
            context = {"result": result, "message": message}

        return HttpResponse(
            json.dumps(context),
            content_type="application/json"
        )

    context = {'u_form': u_form, 'up_form': up_form}
    return render(request, 'users/sign_up.html', context)


'''
Basic view for user sign in
'''


def sign_in(request):
    # redirect if user is already signed in
    if request.user.is_authenticated:
        return redirect(reverse('users:account'))

    a_form = AuthForm()
    result = "error"
    message = "Something went wrong. Please check and try again"

    if request.headers.get('x-requested-with') == 'XMLHttpRequest'  and request.method == "POST":
        a_form = AuthForm(data=request.POST)
        if a_form.is_valid():
            username = a_form.cleaned_data.get('username')
            password = a_form.cleaned_data.get('password')

            # authenticate Django built in authenticate - https://docs.djangoproject.com/en/3.1/ref/contrib/auth/
            user = authenticate(request, username=username, password=password)
            if user is not None:

                # check to see if 2-step verification is active
                if user.userprofile.two_step_active:
                    # create and sends a SMS code
                    token = TokenGenerator()
                    make_token = token.make_token(user)
                    url_safe = urlsafe_base64_encode(force_bytes(user.pk))

                    # create and sends a SMS code
                    sms_code = ActivateTwoStep(user=user, token=make_token)
                    message = 'We have sent you an SMS'
                    result = "perfect"
                    return HttpResponse(
                        json.dumps({"result": result, "message": message, "url_safe": url_safe, "token": make_token}),
                        content_type="application/json"
                    )
                else:
                    login(request, user)
                    message = 'You are now logged in'
                    result = "perfect"

        else:
            message = FormErrors(a_form)

        return HttpResponse(
            json.dumps({"result": result, "message": message}),
            content_type="application/json"
        )
    context = {'a_form': a_form}

    # passes 'token_error' parameter to url to handle a error message
    token_error = request.GET.get("token_error", None)
    if token_error:
        context["token_error"] = "true"
    else:
        context["token_error"] = "false"

    return render(request, 'users/sign_in.html', context)


'''
Basic view for user sign out
'''


def sign_out(request):
    logout(request)
    return redirect(reverse('users:sign-in'))


'''
Basic view for users to request a new password
'''


def forgotten_password(request):
    rp_form = RequestPasswordForm()
    result = "error"
    message = "Something went wrong. Please check and try again"

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        rp_form = RequestPasswordForm(data=request.POST)

        if rp_form.is_valid():

            username = rp_form.cleaned_data.get('email')
            user = User.objects.get(username=username)
            # create a new token
            token = TokenGenerator()
            make_token = token.make_token(user)

            ut = UserToken.objects.create(
                user=user,
                token=make_token,
                is_password=True)

            # send email verification email
            CreateEmail(
                request,
                email_account="donotreply",
                subject='Password reset',
                email=user.username,
                cc=[],
                template="password_email.html",
                token=make_token,
                url_safe=urlsafe_base64_encode(force_bytes(user.pk))
            )
            result = "perfect"
            message = "You will receive an email to reset your password"
        else:
            message = FormErrors(rp_form)

        return HttpResponse(
            json.dumps({"result": result, "message": message}),
            content_type="application/json"
        )
    context = {'rp_form': rp_form}
    return render(request, 'users/forgotten_password.html', context)


'''
Account view for registered users
'''


@login_required
def account(request):
    if request.method == "POST":
        toggle = request.POST.get("toggle")

        up = request.user.userprofile
        if toggle == "on":
            up.two_step_active = True
        else:
            up.two_step_active = False

        up.save()

        return HttpResponse(
            json.dumps({}),
            content_type="application/json"
        )

    context = {}
    # passes 'verified' parameter to url to handle a success message
    verified = request.GET.get("verified", None)
    if verified:
        context["verified"] = "true"
    else:
        context["verified"] = "false"

    return render(request, 'users/account.html', context)


'''
AJAX function to request email view for registered users
'''


@login_required
def email(request):
    result = "error"
    message = "Something went wrong. Please check and try again"

    if request.method == "POST":
        user = request.user
        # create a new token
        token = TokenGenerator()
        make_token = token.make_token(user)
        url_safe = urlsafe_base64_encode(force_bytes(user.pk))

        # Create a usertoken object to store token
        ut = UserToken.objects.create(
            user=user,
            token=make_token,
            is_email=True)

        # send email verification email
        CreateEmail(
            request,
            email_account="donotreply",
            subject='Verify your email',
            email=user.username,
            cc=[],
            template="verification_email.html",
            token=make_token,
            url_safe=url_safe
        )

        result = "perfect"
        message = "We have sent you an email to verify"
        return HttpResponse(
            json.dumps({"result": result, "message": message}),
            content_type="application/json"
        )

    return HttpResponse(
        json.dumps({"result": result, "message": message}),
        content_type="application/json"
    )


'''
Function view to handle verification tokens
'''


def verification(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        ut = UserToken.objects.get(user=user, token=token, is_active=True)
        email_token = ut.is_email
        password_token = ut.is_password

    except(TypeError, ValueError, OverflowError, User.DoesNotExist, UserToken.DoesNotExist):

        # user our RedirectParams function to redirect & append 'token_error' parameter to fire an error message
        return RedirectParams(url='users:sign-in', params={"token_error": "true"})

    # if User & UserToken exist...
    if user and ut:

        # if the token type is_email
        if email_token:

            # deactivate the token now that it has been used
            ut.is_active = False
            ut.save()

            up = user.userprofile
            up.email_verified = True
            up.save()

            # login the user
            login(request, user)

            # user our RedirectParams function to redirect & append 'verified' parameter to fire a success message
            return RedirectParams(url='users:account', params={"verified": "true"})

        # if the token is a password token
        elif password_token:

            fp_form = ForgottenPasswordForm(user=user)
            result = "error"
            message = "Something went wrong. Please check and try again"

            if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
                fp_form = ForgottenPasswordForm(data=request.POST, user=user)

                if fp_form.is_valid():

                    fp_form.save()
                    login(request, user)

                    # deactivate the token now that it has been used
                    ut.is_active = False
                    ut.save()
                    message = "Your password has been updated"
                    result = "perfect"

                else:
                    message = FormErrors(rp_form)

                return HttpResponse(
                    json.dumps({"result": result, "message": message}),
                    content_type="application/json"
                )
            context = {'fp_form': fp_form, "uidb64": uidb64, "token": token}
            return render(request, 'users/verification.html', context)

        # else the token is for 2 step verification
        else:
            ts_form = TwoStepForm()
            result = "error"
            message = "Something went wrong. Please check and try again"

            if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
                ts_form = TwoStepForm(data=request.POST)

                if ts_form.is_valid():

                    two_step_code = ts_form.cleaned_data.get('two_step_code')

                    if two_step_code == ut.two_step_code:

                        user.is_active = True
                        user.save()

                        login(request, user)

                        # deactivate the token now that it has been used
                        ut.is_active = False
                        ut.save()
                        message = "Success! You are now signed in"
                        result = "perfect"
                    else:
                        message = "Incorrect code, please try again."
                else:
                    message = FormErrors(rp_form)

                return HttpResponse(
                    json.dumps({"result": result, "message": message}),
                    content_type="application/json"
                )
            context = {'ts_form': ts_form, "uidb64": uidb64, "token": token}

            return render(request, 'users/two_step_verification.html', context)