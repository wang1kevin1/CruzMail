from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .collection.models import mailstops_master, packages_master

# Create your views here.
@csrf_exempt
def query_package(request):
    print ("hello world")
    #test = mailstops_master.objects.create(mailstop=request.POST.get('new_m'),
    #                                      ms_route=request.POST.get('new_r'))
    params = []    
    index = int(request.POST.get('index'))
    for r in mailstops_master.objects.all()[index:index+10]:
        t = dict(a = r.mailstop,
                 b = r.ms_status,
                 c = r.ms_route
                 )
        params.append(t)
    return JsonResponse(dict(params= params))

def package_delivered(request):
    for package in request.POST.get('list'):
        packages_master.objects.get(pkg_tracking=package.id).update(pkg_status='d')
        print('updaing\n')
    return response

def update_package(request):
    packages_master.objects.get(pkg_tracking=request.POST.get('id')).update(pkg_remarks='test')
    return null


@csrf_exempt
def add_package(request):
    packages_master.objects.create(pkg_tracking = request.POST.get('track'),
                                  #pkg_name = request.POST.get('name'),
                                  #pkg_mailstop = request.POST.get('mailstop'),
                                  pkg_status = 'd',
                                  pkg_sign = request.POST.get('sign'),
                                  pkg_email = request.POST.get('email'),
                                  #pkg_date_rec = 0,
                                  pkg_remarks = request.POST.get('remark'))
    return request

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
