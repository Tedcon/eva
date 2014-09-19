#-*- coding:utf8 -*-
from eva.models import *
from chat.models import *
import datetime

def common(word_list):
    turn_list = {}
    time_list = Pertain.objects.filter(pertain="time")
    turn_list["ask"] = 0
    for word in word_list:
        if word in time_list:
            turn_list["time"] = word
            continue
        if word in ask_list:
            turn_list["ask"] = 1
            continue
        if turn_list.has_key("who"):
            continue
        else :
            turn_list["who"] = word
        if turn_list.has_key("name"):
            continue
        else:
            turn_list["name"] = word
        if turn_list.has_key("value"):
            continue
        else:
            turn_list["value"] = word
        if turn_list.has_key("more"):
            break
        else:
            turn_list["more"] = word
    return turn_list

def easy_split(word):
    word_list = word.split() #根据空格分词
    length = len(word_list)
    return word_list

def auto_chat(word_dict):
    facts = Fact.objects.all()
    log = {}

    if word_dict["ask"]==0:
        is_save = True
    if word_dict.has_key("who"):
        who_ = word_list["who"]
        facts = facts.objects.filter(who = who_ )
        log("who",who_)

    if word_dict.has_key("name"):
        name_ = word_list["name"]
        facts = facts.objects.filter(name = name_)
        log("name",name_)

    if word_dict.has_key("value"):
        value_ = word_list["value"]
        facts = facts.objects.filter(value = value_)
        log("value",value_)

    if word_dict.has_key("more"):
        more_ = word_list["more"]
        facts = facts.objects.filter(more = more_)
        log("more",more_)

    if word_dict.has_key("time"):
        time_ = word_list["time"]
        facts = facts.objects.filter(time = time_)
        log("time",time_)

    if is_save:
        Fact(**log).save()
        res = "save"
        return res
    if facts.count() ==0:
        res = "no res"
        return  res
    else:
        facts = facts.order_by("-time")
        fact = facts[0]
        return fact

