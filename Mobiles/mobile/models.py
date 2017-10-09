# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.name

class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete = models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')
    
    def __unicode__(self):
        return self.name

class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete = models.CASCADE)
    nickname = models.CharField(max_length=15, default='Secondary Phone', verbose_name='eva-nickname')
    description = models.TextField(default='No Statement')
    year = models.PositiveIntegerField(default=2016)
    price = models.PositiveIntegerField(default=0)
    
    def __unicode__(self):
        return self.nickname

class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    description = models.TextField(default='No Statement')
    url = models.URLField(default='http://i.imgur.com/z230eeq.png')
    
    def __unicode__(self):
        return self.description
