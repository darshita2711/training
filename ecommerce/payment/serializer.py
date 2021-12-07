from django.db.models import fields
from django.db.models.base import Model
from rest_framework import  serializers
from. models import *
from django.contrib.auth.models import User

class OrderdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orderdata
        fields = ['orderid','user','transection_id','price','product']
