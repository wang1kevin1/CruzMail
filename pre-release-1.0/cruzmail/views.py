from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

from .collection.models import mailstops_master

# Create your views here.
def new_package(request):
    printf("hello world")
    test = mailstops_master.objects.create(mailstop='test1',
                                           ms_route='w')
    return "ok"

def index(request):
    return render(request, 'index.html')

class HomePageViews(TemplateView):
   template_name = 'index.html'

class ManagePageViews(TemplateView):
    template_name = 'manage.html'

    #def new_package(request):
    #    printf("hello world")
    #    test = mailstops_master.objects.create(mailstop='test1',
    #                                           ms_route='w')
    #    return "ok"

class MenuPageViews(TemplateView):
    template_name = 'menu.html'
