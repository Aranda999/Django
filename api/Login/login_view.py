from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def login_views(request):
    template_view = "signin.html"
    
    #Verifica si el usuario ya esta logueado
    if request.user.is_authenticated and request.user.is_active:
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
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Comprobar si el correo ya está en uso
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya existe.")
        # Comprobar si el nombre de usuario ya está en uso
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
        else:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    is_active = 0)
                user.save()
                messages.success(request, "Usuario registrado con éxito.")
                return redirect('register_view')  # Redirige a la vista de login
            except Exception as e:
                messages.error(request, "Error al registrar el usuario:" + str(e))

    return render(request, template_view)

#Vista para salir
def logout_view(request):
    logout(request) 
    return redirect('login_view') 
