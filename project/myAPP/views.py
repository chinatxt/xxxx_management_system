# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.

import time
import datetime
from .models import Hotel, Order, RoomInfo, Customer

def about(request):
    title = 'DJango Hotel'
    hotel = Hotel.objects.get(name='DJango Hotel')
    name = hotel.name
    description = hotel.description
    address = hotel.address

    return render_to_response('about.html',{'title':title,'name':name,'description':description,'address':address})


def index(request):
    hotel = Hotel.objects.get(name='DJango Hotel')
    description = hotel.description

    return render_to_response('index.html',{'description':description})

def orderResult(request):
    tempCustomer = Customer()
    tempCustomer.tel = request.GET['tel']
    tempCustomer.name = request.GET['name']
    tempCustomer.cardid = request.GET['cardid']
    tempCustomer.save()

    tempOrder = Order()
    tempOrder.name = request.GET['name']
    tempOrder.tel = request.GET['tel']
    tempOrder.cardid = request.GET['cardid']
    tempOrder.roomtype = request.GET['roomtype']

    begin = request.GET['begin']
    end = request.GET['end']
    tempOrder.begin = (datetime.datetime.strptime(begin , '%Y-%m-%d')).date()
    tempOrder.end = (datetime.datetime.strptime(end , '%Y-%m-%d')).date()
    period = (tempOrder.end - tempOrder.begin).days

    price = 0

    if tempOrder.roomtype == 'standard':
        price = (RoomInfo.objects.get(name = '标准间')).price

    elif tempOrder.roomtype =='better':
        price = (RoomInfo.objects.get(name = '豪华间')).price

    elif tempOrder.roomtype =='president':
        price = (RoomInfo.objects.get(name = '总统间')).price


    tempOrder.totalprice = period * price
    tempOrder.save()

    tel = request.GET['tel']
    begin = request.GET['begin']

    return render_to_response('orderresult.html',{'orderid':tempOrder.id})

def order(request):
    return render_to_response('order.html')

def rooms(request):
    roomInfoList=RoomInfo.objects.all()
    return render_to_response('rooms.html',{'roomInfoList':roomInfoList})
