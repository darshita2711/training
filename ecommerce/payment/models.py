from django.db import models
from django.contrib.auth.models import User
from myapp.models import *
# Create your models here.

class Orderdata(models.Model):
    orderid=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    transection_id=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

