from statistics import mode
from unicodedata import category
from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=60)
    product_desc = models.CharField(max_length=500)
    category = models.CharField(max_length=60,default="")
    subCategory = models.CharField(max_length=60,default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to ='shop/images',default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=60)
    contact_email = models.CharField(max_length=80)
    contact_phone = models.IntegerField()
    contact_desc = models.CharField(max_length=100,default="")
   

    def __str__(self):
        return self.contact_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=4000)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    phone = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()

    def __str__(self):
        return self.name