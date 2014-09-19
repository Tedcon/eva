#-*- coding:utf8 -*-
from eva.models import *
from chat.models import *
import datetime

def common(word_list):
    turn_list = {}
    turn_list["ask"] = 0
    pertain = Pertain.objects.all()
    for word in word_list:
        p = pertain.objects.filter(word=word)[0]
        if p:
            if p.pertain:
                ps = pertain.objects.filter(word=p.pertain) #找到同义词
                turn_list[ps.wordtype] = word
        else:
            thistype = ask(p)
            turn_list[thistype] = word

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

def ask(word):
    pass
def main_deal(long_word):
    word_list = easy_split(long_word)
    word_dict = common(word_list)
    res = auto_chat(word_dict)
    return res
