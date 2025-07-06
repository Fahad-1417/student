from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import StudentProfile
from .forms import StudentProfileForm


def home_view(request):
    return render(request, 'home.html')



def student_services_view(request):
    return render(request, 'student/services.html')


@login_required
def profile_view(request):
    user = request.user
    try:
        profile = user.studentprofile
    except StudentProfile.DoesNotExist:
        profile = None

    return render(request, 'student/profile.html', {
        'user': user,
        'profile': profile
    })
@login_required
def edit_profile(request):
    user = request.user
    try:
        profile = user.studentprofile
    except StudentProfile.DoesNotExist:
        profile = StudentProfile.objects.create(user=user)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=profile)

        # تحقق من الاسم والبريد أولًا
        first_name = request.POST.get('first_name', '').strip()
        email = request.POST.get('email', '').strip()

        if not first_name or not email:
            form.add_error(None, "يرجى إدخال الاسم الكامل والبريد الإلكتروني.")
        else:
            user.first_name = first_name
            user.email = email
            user.save()

            if form.is_valid():
                form.save()
            return redirect('profile')

    else:
        form = StudentProfileForm(instance=profile)

    return render(request, 'student/edit_profile.html', {
        'user': user,
        'form': form
    })
