"""
URL configuration for alx_travel_app project.
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('listings.urls')),  # Comment this out for now
]