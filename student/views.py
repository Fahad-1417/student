from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages  # ✅ لإظهار رسالة بعد الدفع
from .models import StudentProfile, Enrollment
from .forms import StudentProfileForm
from instructor.models import ProfessionalCourse  # ✅ استبدال Course بالموديل الصحيح


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


@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(ProfessionalCourse, id=course_id)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect('my_courses')


@login_required
def my_courses_view(request):
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course')
    return render(request, 'student/my_courses.html', {'enrollments': enrollments})


# ✅ صفحة الدفع عند الضغط على "اشترك الآن"
@login_required
def payment_view(request, course_id):
    course = get_object_or_404(ProfessionalCourse, id=course_id)

    if request.method == 'POST':
        Enrollment.objects.get_or_create(user=request.user, course=course)
        messages.success(request, f"تم الاشتراك بنجاح في دورة: {course.title}")
        return redirect('home')  # التوجيه للصفحة الرئيسية بعد الدفع

    return render(request, 'payment.html', {'course': course})
