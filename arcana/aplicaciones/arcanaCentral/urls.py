
from django.urls import path
from .views import arcanaHome



urlpatterns = [
    path('', arcanaHome, name='arcanaHome'),
]