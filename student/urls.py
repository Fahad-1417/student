from django.urls import path
from django.http import HttpResponse
from .views import home_view

urlpatterns = [
    
    path('', home_view, name='home'),
]
