# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:53:58 2019

@author: Matt Macarty
"""

from django.urls import path
from . import views

urlpatterns = [
       path('', views.index, name='index'),
       path('quotes', views.quotes, name='quotes'),
        ]
