#-*- coding:utf8 -*-

from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response 

from chat.chat import main_deal

def home(req):
    t = get_template('home.html')
    c = RequestContext(req,locals())
    return HttpResponse(t.render(c))

def chat(req):
    word = req.POST.get("word")
    res = main_deal(word)

    return HttpResponse(res)
