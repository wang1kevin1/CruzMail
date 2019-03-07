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

class mailstops_master(models.Model):
    mailstop  = models.CharField(max_length = 15, primary_key = True)

    ms_name = models.CharField(max_length = 30)

    ms_route_choice = (
        ('W', 'W'),
        ('C', 'C'),
        ('E', 'E'))
    ms_route  = models.CharField(max_length = 1, choices = ms_route_choice)
    
    ms_route_order = models.CharField(max_length = 3)

    ms_status_choice = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),)
    ms_status = models.CharField(max_length = 8, choices = ms_status_choice, default = 'Active')


class people_master(models.Model):
    name        = models.CharField(max_length = 20, primary_key = True)
    ppl_email   = models.CharField(max_length = 40)

    ppl_status_choice = (
        ('Available', 'Available'),
        ('Away', 'Away'),)
    ppl_status = models.CharField(max_length = 9, choices = ppl_status_choice, default = 'Available')

    mailstop = models.CharField(max_length = 20)#models.ForeignKey(mailstops_master, on_delete=models.DO_NOTHING)

    # allows for people with the same name to reside in system as long as different mailstops. Messes up request.POST.get
    #class Meta:
        #unique_together = (('name', 'mailstop'),)


class packages_master(models.Model):
    pkg_tracking = models.CharField(max_length = 20, primary_key = True)
    name         = models.CharField(max_length = 20)#models.ForeignKey(people_master, on_delete=models.DO_NOTHING)
    mailstop     = models.CharField(max_length = 20)#models.CharField(max_length = 20, primary_key = True)


    pkg_status= models.CharField(max_length = 20)

    pkg_sign = models.CharField(max_length = 20)
    
    
    pkg_email = models.CharField(max_length = 20)

    pkg_weight   = models.CharField(max_length = 7,  null = False)
    pkg_date_rec = models.DateField(default = datetime.date.today)
    pkg_date_del = models.DateField(default = datetime.date.today)
    pkg_remarks  = models.CharField(max_length = 144)
