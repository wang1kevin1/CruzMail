# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from django.contrib.auth.tokens import *
import datetime
from django.http import HttpResponse

# Create your models here.
class User_Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    users = User.objects.all()
    #print("hello")
    #bio = models.CharField(max_length=2000, default="")
    #private_account = models.BooleanField(default=True)

class mailstops_master(models.Model):
    mailstop  = models.CharField(max_length = 20, primary_key = True)

    ms_status_choice = (
        ('0', 'active'),
        ('1', 'inactive'),)
    ms_status = models.CharField(max_length = 1, choices = ms_status_choice, default = '0')
    
    ms_route_choice = (
        ('w', 'West'),
        ('c', 'central'),
        ('e', 'east'))
    ms_route  = models.CharField(max_length = 1, choices = ms_route_choice)
    
    


class people_master(models.Model):
    name     = models.CharField(max_length = 20, primary_key = True)
    email    = models.CharField(max_length = 20)
    #mailstop = models.ForeignKey(mailstops_master, on_delete=models.DO_NOTHING)




class packages_master(models.Model):
    pkg_tracking = models.CharField(max_length = 20, primary_key = True)
    name         = models.CharField(max_length = 20)#models.ForeignKey(people_master, on_delete=models.DO_NOTHING)
    mailstop     = models.CharField(max_length = 20)#models.CharField(max_length = 20, primary_key = True)


    pkg_status_choice = (
        ('r', 'recieved'),
        ('d', 'delivered'))
    pkg_status   = models.CharField(max_length = 1, choices = pkg_status_choice)

    pkg_sign_choice = (
        ('y', 'yes'),
        ('n', 'no'))
    pkg_sign     = models.CharField(max_length = 1, choices = pkg_sign_choice, default = 'n')
    
    
    pkg_email_choice = (
        ('y', 'yes'),
        ('n', 'no'))
    pkg_email    = models.CharField(max_length = 1, choices = pkg_email_choice, default = 'y') 

    pkg_weight_choice = (
        ('s', '1 to 5'),
        ('m', '6 to 15'),
        ('l', 'over 16'))
    pkg_weight   = models.CharField(max_length = 1, choices = pkg_weight_choice, null = False)
    pkg_date_rec = models.DateField(default = datetime.date.today)
    pkg_date_del = models.DateField(default = datetime.date.today)
    pkg_remarks  = models.CharField(max_length = 144)
