"""cargas_fisicas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from app_principal.views import home,multimedia,formulario,saberes
from django.urls import path
#from app_principal.views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),# url login
    path('home/',(home) , name='login'),# principal
    path('multimedia/',(multimedia) , name='multimedia'),# muestra de ejecicios
    path('formulario/',(formulario) , name='formulario'),# 
    path('saberes/',(saberes) , name='saberes'),# 
    
]
