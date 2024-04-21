from django.contrib import admin
from django.urls import path, include  # make sure include is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('', include('login.urls')),  # Route API requests to tasks.urls
    path('', include('accounts.urls')),  # Route API requests to tasks.urls
    path('api/', include('cashflow.urls')),
    path('api/', include('notifications.urls')),
    
    
   
]
