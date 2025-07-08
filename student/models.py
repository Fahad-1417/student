from django.db import models
from django.contrib.auth.models import User
from instructor.models import ProfessionalCourse  # ✅ استيراد الموديل الصحيح من instructor


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, verbose_name="رقم الجوال", blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', verbose_name="الصورة الشخصية", blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# ✅ موديل Course محفوظ بدون حذف لأغراض مستقبلية
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
   
    def __str__(self):
        return self.title


# ✅ تعديل الربط ليستخدم ProfessionalCourse بدلاً من Course
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(ProfessionalCourse, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
