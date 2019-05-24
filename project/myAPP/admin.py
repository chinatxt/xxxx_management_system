# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'room_id', 'begin', 'end')

class customerAdmin(admin.ModelAdmin):
    list_display = ('tel', 'name', 'gender')

admin.site.register(Customer, customerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Order, OrderAdmin)
