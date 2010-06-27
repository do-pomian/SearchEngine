'''
Created on Jun 23, 2010

@author: dpomian
'''
from SearchEngine.mysearchengine.models import Store
from SearchEngine.mysearchengine.models import StoreDetails
from SearchEngine.mysearchengine.models import Producers
from SearchEngine.mysearchengine.models import Products
from SearchEngine.mysearchengine.models import Categories

from django.contrib import admin

admin.site.register(Store)
admin.site.register(StoreDetails)
admin.site.register(Producers)
admin.site.register(Products)
admin.site.register(Categories)