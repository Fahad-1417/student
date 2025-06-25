from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # اجعل صفحة الطالب هي الرئيسية
    path('', include('student.urls')),
    
    path('student/', include('student.urls')),
    path('instructor/', include('instructor.urls')),
    path('dashboard/', include('dashboard.urls')),
]
