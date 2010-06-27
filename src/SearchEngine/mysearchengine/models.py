from django.db import models

# Create your models here.
class Store (models.Model):
    StoreName = models.CharField (max_length=200)
    def __unicode__(self):
        return self.StoreName
    
class StoreDetails (models.Model):
    Store = models.ForeignKey(Store)
    StoreAddress = models.CharField (max_length=200)
    StorePhone = models.CharField (max_length=14)
    
    def __unicode__(self):
        return self.Store.StoreName + ', ' + self.StoreAddress
    
class Producers (models.Model):
    ProducerName = models.CharField (max_length=200)
    def __unicode__(self):
        return self.ProducerName
    
class Categories (models.Model):
    CategoryName = models.CharField (max_length=200)
    def __unicode__(self):
        return self.CategoryName
    
class Products (models.Model):
    ProductName = models.CharField (max_length=200)
    Price = models.IntegerField ()
    Producer = models.ForeignKey (Producers)
    Category = models.ForeignKey (Categories)
    Store = models.ForeignKey (Store)
    
    def __unicode__(self):
        return self.ProductName