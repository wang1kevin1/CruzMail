from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template  import RequestContext


from .models import mailstops_master
from django.views.generic import ManagePageViews

# Create your views here.
def new_package(request):
    test = mailstops_master.objects.create(mailstop='test1', 
                                           ms_route='w')
    return "ok"

