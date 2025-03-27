"""
URL configuration for DjangoApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from django.contrib import admin
from django.urls import path
from api.Login.login_view import (
    login_views,logout_view,
    register_view)
from api.home.home_view import (home_views,
    forms_view, table_view,chart_view,widget_view,camera)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_views,name="login_view"),    
    path('register/',register_view,name="register_view"),
    path('logout/',logout_view,name="logout"),        
    path('',home_views,name="home"),
    path('home/',home_views,name="home"),
    path('forms/',forms_view,name="form"),
    path('table/',table_view,name="table"),
    path('chart/',chart_view,name="chart"),
    path('widget/',widget_view,name="widget"),
    path('camera/',camera,name="camera"),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)