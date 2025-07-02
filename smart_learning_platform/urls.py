from django.contrib import admin
from django.urls import path, include
from dashboard.views import login_view, logout_view
from django.views.generic import TemplateView
from dashboard.views import login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('instructor/', include('instructor.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # الصفحة الرئيسية
    path('new-account/', TemplateView.as_view(template_name='dashboard/new_account.html'), name='new_account'),
    path('', include('student.urls')),

  # الصفحة الرئيسية
]
