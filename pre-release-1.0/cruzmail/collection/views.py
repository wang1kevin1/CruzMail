from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import *
from .models import User_Profile

def collection(request):
	profile = get_object_or_404(User_Profile)
	return render(request, 'users.html', {'profile': profile})
