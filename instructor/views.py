from django.shortcuts import render
from .models import ProfessionalCourse
# from instructor.models import Course




def courses_view(request):
    courses = ProfessionalCourse.objects.all()
    return render(request, 'instructor/courses.html', {'courses': courses})
