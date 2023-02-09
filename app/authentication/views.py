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
            return redirect('core:index')
        else:
            messages.error(
                request, 'Unable to authenticate with provided credentials.')
            return redirect('authentication:login')
    else:
        return render(request, 'authentication/login.html')


def logout_user(request):
    logout(request)
    return redirect('core:index')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email'] or ""
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if get_user_model().objects.filter(name=username).exists():
            messages.error(request, "Username already exists")
            return redirect('authentication:register')
        if get_user_model().objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('authentication:register')

        if password1 == "" or password2 == "" or password1 != password2:
            messages.error(request, "Passwords don't match.")
            return redirect('authentication:register')
        user = get_user_model().objects.create_user(
            name=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Account creation successful.')
        return redirect('authentication:login')

    else:
        return render(request, 'authentication/register.html')
