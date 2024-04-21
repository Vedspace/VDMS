# location/views.py

from django.http import JsonResponse
from .models import UserLocation
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

@csrf_exempt
@login_required
def update_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data['latitude']
        longitude = data['longitude']
        UserLocation.objects.create(user=request.user, latitude=latitude, longitude=longitude)
        return JsonResponse({"status": "success"}, safe=False)
    return JsonResponse({"status": "error"}, safe=False)

# location/ur

from django.urls import path
from .views import update_location

urlpatterns = [
    path('update/', update_location, name='update-location'),
]
