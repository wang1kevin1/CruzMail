from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Permission
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .collection.models import mailstops_master, packages_master

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

# PACKAGE VIEWS
@csrf_exempt
def query_package(request):

    #if user is not None:
    #  login(request, user)
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
    logout(request)
    t = packages_master.objects.get(pkg_tracking=request.POST.get('pkg_tracking'))
    t.pkg_status='received'
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
                                  pkg_status = 'delivered',
                                  pkg_sign = request.POST.get('sign'),
                                  pkg_email = request.POST.get('email'),
                                  pkg_weight = '1 to 5',
                                  pkg_remarks = request.POST.get('remark'))
    return JsonResponse(dict(test="ok"))

# MAILSTOP VIEWS.
@csrf_exempt
def query_mailstop(request):
    params = []
    search = request.POST.get('search')
    index = int(request.POST.get('index'))
    for r in mailstops_master.objects.all():
      if search is None or (len(search) <= len(r.mailstop) and search == r.mailstop[0:len(search)]):
        t = dict(mailstop       = r.mailstop,
                 ms_name        = r.ms_name,
                 ms_route       = r.ms_route,
                 ms_route_order = r.ms_route_order,
                 ms_status      = r.ms_status
                )
        params.append(t)
    return JsonResponse(dict(params= params))

@csrf_exempt
def activate_mailstop(request):
    t = mailstops_master.objects.get(mailstop=request.POST.get('mailstop'))
    t.ms_status='Active'
    t.save()
    return JsonResponse(dict(test="ok"))

@csrf_exempt
def deactivate_mailstop(request):
    t = mailstops_master.objects.get(mailstop=request.POST.get('mailstop'))
    t.ms_status='Inactive'
    t.save()
    return JsonResponse(dict(test="ok"))

@csrf_exempt
def update_mailstop(request):
    t = mailstops_master.objects.get(mailstop=request.POST.get('ms_id'))
    t.ms_name         = request.POST.get('ms_name')
    t.ms_route        = request.POST.get('ms_route')
    t.ms_route_order  = request.POST.get('ms_route_order')
    t.ms_status       = request.POST.get('ms_status')
    t.save()
    return JsonResponse(dict(test="ok"))

@csrf_exempt
def add_mailstop(request):
    mailstops_master.objects.create(mailstop        = request.POST.get('ms_id'),
                                    ms_name         = request.POST.get('ms_name'),
                                    ms_route        = request.POST.get('ms_route'),
                                    ms_route_order  = request.POST.get('ms_route_order'),
                                    ms_status       = 'Active'
                                   )
    return JsonResponse(dict(test="ok"))

# ADMIN VIEWS
@csrf_exempt
def get_users(request):
  name_users = []
  
  
  for key in User.objects.all():
    names = dict(
      username = key.username
      )
    name_users.append(names)

  return JsonResponse(dict(user_list = name_users))

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/account/login')
def manage(request):
    return render(request, 'manage.html')

@login_required(login_url='/account/login')
def menu(request):
  return render(request, 'menu.html')


@login_required(login_url='/account/login')
def collection(request):
  return render(request, 'users.html')


@login_required(login_url='/account/login')
def mailstop(request):
  return render(request, 'mailstop.html')

