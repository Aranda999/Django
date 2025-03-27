from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.home.value_const import LOGIN_URL
from api.models import Imagen
# Create your views here.

#Create constantes

@login_required(login_url=LOGIN_URL)
def home_views(request):
    template_view = "index.html"
    imagenes = Imagen.objects.all()
    context = {
        'imagenes':imagenes,
    }
    return render(request,template_view,context)

def forms_view(request):
    template_view = "form.html"
    return render(request,template_name=template_view)

def table_view(request):
    template_view = "table.html"
    return render(request,template_name=template_view)

def chart_view(request):
    template_view = "chart.html"
    return render(request,template_name=template_view)

def widget_view(request):
    template_view = "widget.html"
    return render(request,template_name=template_view)

def camera(request):
    template_view = "camera.html"
    return render(request,template_name=template_view)

