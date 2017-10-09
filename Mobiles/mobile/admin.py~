# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mobile import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pmodel', 'nickname', 'price', 'year')
    ordering = ('-price',)
    search_fields = ('nickname',)
admin.site.register(models.Maker)
admin.site.register(models.PModel)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.PPhoto)
