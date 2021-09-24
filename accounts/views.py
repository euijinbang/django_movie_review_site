from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.views.decorators.http import require_http_methods, require_POST

# Create your views here.

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('community:index')
    else:
        pass
    form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request)
        return redirect('community:index')
    else:
        pass
    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('community:index')
    else:
        pass

def change_password():
    pass
