from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_views(request):
    template_view = "signin.html"
    
    #Verifica si el usuario ya esta logueado
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'invalid credentials')
    return render(request,template_view)

#Vista para registro
def register_view(request):
    template_view = "signup.html"
    return render(request,template_name=template_view)

#Vista para salir
def logout_view(request):
    logout(request) 
    return redirect('login_view') 
