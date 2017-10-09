# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
# Create your views here.

def homepage(request, testmode):
    template = get_template('index.html')
    return HttpResponse(template.render())

def about(request, author_no):
    html = "<h2>Here is Author:{}'s about page!</h2><hr>".format(author_no)
    return HttpResponse(html)

def listing(request, list_date):
    html = "<h2>List Date is {}</h2><hr>".format(list_date)
    return HttpResponse(html)

def post(request, yr, mon, day, post_num):
    html = "<h2>{}/{}/{}:Post Number:{}</h2><hr>".format(yr, mon, day, post_num)
    return HttpResponse(html)

def company(request):
    return HttpResponse('Company of mine')

def index(request, tvno='0'):
    tv_list = []
    template = get_template('index.html')
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    html = template.render(locals())
    return HttpResponse(html)
