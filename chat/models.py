#-*- coding:utf8 -*-
from django.db import models

# Create your models here.

class Log(models.Model):
    time = models.CharField()
    who = models.IntergerField() # user id
    chats = models.CharField() 

class Pertain(models,Model):
    word = models.CharField()
    pertain = models.CharField()