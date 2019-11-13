from django.db import models

class MarchantModel(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=30   )

class ProductModel(models.Model):
    p_no = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50, unique=True)
    p_price = models.FloatField()
    p_quantity = models.IntegerField()