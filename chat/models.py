#-*- coding:utf8 -*-
from django.db import models

# Create your models here.

class Log(models.Model):
    time = models.CharField(max_length=20)
    who = models.CharField(max_length=20) # user id
    chats = models.CharField(max_length=50) 

class Pertain(models.Model):
    word = models.CharField(max_length=20)
    pertain = models.CharField(max_length=20)
    wordtype = models.CharField(max_length=10)

class Fact(models.Model):
    time = models.CharField(max_length=20)
    who = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    more = models.CharField(max_length=20)