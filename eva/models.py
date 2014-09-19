#-*- coding:utf8 -*-

from django.db import models

class Fact(models.Model):
    time = models.CharField()
    who = models.CharField()
    name = models.CharField()
    value = models.CharField()
    more = models.CharField()

