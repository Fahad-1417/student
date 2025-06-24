from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ربط تطبيق الطالب
    path('student/', include('student.urls')),

    # ربط تطبيق المعلم
    path('instructor/', include('instructor.urls')),

    # ربط تطبيق الإدارة
    path('dashboard/', include('dashboard.urls')),
]
