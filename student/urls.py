from django.urls import path
from django.http import HttpResponse
from .views import home_view
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('services/', views.student_services_view, name='student_services'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('courses/<int:course_id>/enroll/', views.enroll_in_course, name='enroll_course'),
    path('my-courses/', views.my_courses_view, name='my_courses'),

    # ✅ رابط صفحة الدفع
    path('payment/<int:course_id>/', views.payment_view, name='payment'),
]
