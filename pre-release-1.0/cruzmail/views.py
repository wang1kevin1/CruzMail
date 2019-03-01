from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .collection.models import mailstops_master, packages_master

# Create your views here.
@csrf_exempt
def query_package(request):

    #print ("hello world")
    #test = mailstops_master.objects.create(mailstop=request.POST.get('new_m'),
    #                                      ms_route=request.POST.get('new_r'))
    params = []    
    search = request.POST.get('search')
    index = int(request.POST.get('index'))
    for r in packages_master.objects.all():
        if search is None or (len(search) <= len(r.pkg_tracking) and search == r.pkg_tracking[0:len(search)]):
            t = dict(a = r.pkg_tracking,
                     b = r.pkg_status,
                     c = r.pkg_date_rec,
                     name = r.name,
                     mailstop = r.mailstop,
                     sign = r.pkg_sign,
                     weight = r.pkg_weight,
                     email = r.pkg_email
                    )
            params.append(t)
    return JsonResponse(dict(params= params))

@csrf_exempt
def package_delivered(request):

    t = packages_master.objects.get(pkg_tracking=request.POST.get('pkg_tracking'))
    t.pkg_status='r'
    t.save()
    return JsonResponse(dict(test="ok"))

@csrf_exempt
def update_package(request):

    t = packages_master.objects.get(pkg_tracking=request.POST.get('track'))
    t.name =       request.POST.get('name')
    t.pkg_email =  request.POST.get('email')
    t.pkg_weight = request.POST.get('weight')
    t.pkg_sign =   request.POST.get('sign')
    t.save()
    return JsonResponse(dict(test="ok"))


@csrf_exempt
def add_package(request):
    packages_master.objects.create(pkg_tracking = request.POST.get('track'),
                                  name = request.POST.get('name'),
                                  mailstop = request.POST.get('mailstop'),
                                  pkg_status = 'd',
                                  pkg_sign = request.POST.get('sign'),
                                  pkg_email = request.POST.get('email'),
                                  #pkg_date_rec = 0,
                                  pkg_remarks = request.POST.get('remark'))
    return JsonResponse(dict(test="ok"))

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

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

class CollectionPageViews(TemplateView):
    template_name = 'users.html'

