# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    tel = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    gender = models.BooleanField(default = 1)

class Room(models.Model):
    name = models.CharField(max_length = 30)
    price = models.IntegerField(null = True, blank = True)
    description = models.TextField(default = '')
    img_path = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class Order(models.Model):
    customer_id = models.IntegerField(default = 0)
    room_id = models.IntegerField(default = 0)
    begin = models.DateField()
    end = models.DateField()
