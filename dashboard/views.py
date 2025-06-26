from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # ✅ توجيه المستخدم للصفحة الرئيسية بعد تسجيل الدخول
        else:
            return render(request, 'dashboard/login.html', {'error': 'اسم المستخدم أو كلمة المرور غير صحيحة.'})
    return render(request, 'dashboard/login.html')  # عرض نموذج تسجيل الدخول في حال GET


def logout_view(request):
    logout(request)
    return redirect('/')  # ✅ توجيه المستخدم للصفحة الرئيسية بعد تسجيل الخروج


def about_view(request):
    return render(request, 'dashboard/about.html')