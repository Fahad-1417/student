from django.shortcuts import render
from .models import ProfessionalCourse



def courses_view(request):
    courses = ProfessionalCourse.objects.all()
    return render(request, 'instructor/courses.html', {'courses': courses})
