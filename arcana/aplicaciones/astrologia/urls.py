
from django.urls import path
from .views import *



urlpatterns = [
    path('', astrologia, name='astrologia'),
    path('post/', post, name='post'),
]