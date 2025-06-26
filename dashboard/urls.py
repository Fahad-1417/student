from django.urls import path
from django.http import HttpResponse
from . import views
from .views import about_view

urlpatterns = [
    path('', lambda request: HttpResponse("لوحة الإدارة")),
    path('login/', views.login_view, name='dashboard-login'),
    path('about/', about_view, name='about'),

    ]
