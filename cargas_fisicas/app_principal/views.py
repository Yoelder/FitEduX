from django.shortcuts import render,redirect
from django.contrib.auth import logout ,login
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout ,login

#from app1.models import Curso

def home(request):

    return render(request, 'home.html')


def multimedia(request):
    
    return render(request, 'muestra.html')

def formulario(request):
    
    return render(request, 'formulario_inicial.html')

def saberes(request):
    
    return render(request, 'saber.html')

