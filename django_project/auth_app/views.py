from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import RegisterForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username-field']
        password = request.POST['password-field']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/lms/welcome')
        else:
            error_msg = "Bad credentials"
    else:
        error_msg = 'Some err msg'
    return render(request, "login.html", context={"error_msg": error_msg})


def logout_view(request):
    logout(request)
    return redirect(login_view)


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(login_view)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

