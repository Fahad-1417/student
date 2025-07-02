from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')



def student_services_view(request):
    return render(request, 'student/services.html')