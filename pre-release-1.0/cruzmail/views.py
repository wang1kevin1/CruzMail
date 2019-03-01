from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

class HomePageViews(TemplateView):
   template_name = 'index.html'

class ManagePageViews(TemplateView):
    template_name = 'manage.html'

class MenuPageViews(TemplateView):
    template_name = 'menu.html'

class CollectionPageViews(TemplateView):
    template_name = 'users.html'

