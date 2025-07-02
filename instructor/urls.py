from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', lambda request: HttpResponse("واجهة المعلم")),
    path('courses/', views.courses_view, name='professional_courses'),

]
