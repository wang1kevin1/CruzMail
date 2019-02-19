# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from django.contrib.auth.tokens import *

# Create your models here.
class User_Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	users = User.objects.all()
	bio = models.CharField(max_length=2000, default="")
	private_account = models.BooleanField(default=True)