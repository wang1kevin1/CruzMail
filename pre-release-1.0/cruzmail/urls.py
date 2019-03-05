"""cruzmail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from .import views

#new.....
from .views import HomePageViews, ManagePageViews, MenuPageViews, CollectionPageViews
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^index', views.index, name="index"),
    url(r'^admin/', admin.site.urls),
   

    path('manage/', ManagePageViews.as_view(), name='manage'),
    path('collection/', CollectionPageViews.as_view(), name='collection'),
    path('',        HomePageViews.as_view(),   name='home'),
    path('menu/', MenuPageViews.as_view(), name='menu'),
    #path('collection/', CollectionPageViews>as_view(), name='users'),

    url(r'^account/', include('cruzmail.account.urls')),
    # url(r'^inbox/', include('cruzmail.inbox.urls'))

    #write new python urls here
    #url(r'collection/^$',views.new_package, name='new_package')
    url(r'^query_package', views.query_package, name='new_package'),
    url(r'^package_delivered', views.package_delivered, name='package_delivered'),
    url(r'^update_package', views.update_package, name='update_package'),
    url(r'^add_package', views.add_package, name='add_package'),

    url(r'^get_users', views.get_users, name='get_users'),
    url(r'^get_emails', views.get_emails, name='get_emails'),


]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
