from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .collection.models import mailstops_master

# Create your views here.
@csrf_exempt
def new_package(request):
    print ("hello world")
    test = mailstops_master.objects.create(mailstop=request.POST.get('new_m'),
                                           ms_route=request.POST.get('new_r'))
    params = []
    for r in mailstops_master.objects.all():
        t = dict(a = r.mailstop,
                 b = r.ms_status,
                 c = r.ms_route
                 )
        params.append(t)
    return JsonResponse(dict(params= params))

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
