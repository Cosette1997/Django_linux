# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.

def carlist(request, maker=0):
    value = False
    l = ['eva', 'adam', 'ashley']
    msg = 'jhvjvuvuviuvyvhfhtdgsfsfdsfhch'
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [
               [{'model': 'Fiesta', 'price': 203500},
                {'model': 'Focus', 'price': 605000},
                {'model': 'Mustang', 'price': 900000}],
               [{'model': 'Fit', 'price': 450000},
                {'model': 'City', 'price': 150000},
                {'model': 'NSX', 'price': 1200000}],
               [{'model': 'Mazda3', 'price': 329999},
                {'model': 'Mazda5', 'price': 603000},
                {'model': 'Mazda6', 'price': 850000}],
             ]
    maker = int(maker)
    maker_name = car_maker[maker]
    cars = car_list[maker]
    template = get_template('carlist.html')
    html = template.render(locals())
    return HttpResponse(html)
