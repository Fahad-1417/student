from django.db import models
from django.contrib.auth.models import User

class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.specialty}"



class ProfessionalCourse(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الدورة")
    description = models.TextField(verbose_name="وصف الدورة")
    image = models.ImageField(upload_to='courses/', verbose_name="صورة الدورة")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="سعر الدورة (ريال)", null=True, blank=True )
    duration = models.CharField(max_length=100,verbose_name="مدة الدورة",null=True, blank=True )
    start_date = models.DateField(verbose_name="تاريخ بداية الدورة",null=True, blank=True )
    

    def __str__(self):
        return self.title