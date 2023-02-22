from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.

def home (request):
    return render(request, "home.html")

    
