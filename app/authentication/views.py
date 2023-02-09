from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            messages.error(
                request, 'Unable to authenticate with provided credentials.')
            return redirect('authentication:login')
    else:
        return render(request, 'authentication/login.html')


def logout_user(request):
    logout(request)
    return redirect('core:home')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email', False)
        is_teacher = request.POST.getlist('is_teacher', False) and True
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if get_user_model().objects.filter(name=username).exists():
            messages.error(request, "Username already exists")
            return redirect('authentication:register')
        if email and get_user_model().objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('authentication:register')

        if password1 == "" or password2 == "" or password1 != password2:
            messages.error(request, "Passwords don't match.")
            return redirect('authentication:register')

        if email:
            user = get_user_model().objects.create_user(
                name=username, email=email, password=password1, is_teacher=is_teacher)
        else:
            user = get_user_model().objects.create_user(
                name=username, password=password1, is_teacher=is_teacher)
        user.save()
        messages.success(request, 'Account creation successful.')
        return redirect('authentication:login')

    else:
        return render(request, 'authentication/register.html')
