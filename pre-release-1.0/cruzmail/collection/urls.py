from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
	url(r'^$', views.collection, name='User_Profile'),
	#url(r'^users', views.users, name='users'),

]