from django.db import models

# Create your models here.

class Product(models.Model):

    Product_name=models.CharField(max_length=200,null=True)
    Product_code=models.CharField(max_length=200,null=True)
    Price=models.FloatField(default=0)
    Gst=models.IntegerField(default=0) 
