# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from mysite.models import Product
import random
from django.template.loader import get_template

# Create your views here.
def listing(request):
    products = Product.objects.all()
    template = get_template('list.html')
    html = template.render({'products': products})
    return HttpResponse(html)

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('Not Found')
    template = get_template('disp.html')
    html = template.render({'product': p})
    return HttpResponse(html)

def about(request):
    template = get_template('about.html')
    html = template.render()
    return HttpResponse(html)

def index(request):
    template = get_template('index.html')
    quotes = ['Where is there dignity unless there is honesty?',
              'When you fish for love, bait with your heart, not\
               your brain.',
              'Man is what he believes.',
              'Autumn is a second spring when every leaf is a flower.'
             ]
    return HttpResponse(template.render({'quote': random.choice(quotes)}))
