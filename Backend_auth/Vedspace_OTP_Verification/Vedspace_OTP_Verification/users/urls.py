# from django.conf.urls import url
from django.urls import path,re_path
from . import views

# 
app_name = "users"

urlpatterns = [
	
	path('', views.sign_in, name="sign-in"),
	re_path(r'^sign-up', views.sign_up, name="sign-up"),
	re_path(r'^sign-out', views.sign_out, name="sign-out"),
	re_path(r'^forgotten-password', views.forgotten_password, name="forgotten-password"),
	re_path(r'^email', views.email, name="email"),
	re_path(r'^account', views.account, name="account"),
	re_path(r'^verification/(?P<uidb64>.+)/(?P<token>.+)/$',views.verification, name='verification'),
	]