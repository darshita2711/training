from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from myapp.models import *


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['price']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Order
        # fields['price'].widget.attrs['readonly'] = True
        fields=['first_name','last_name','price','mobileno','city','state','address','pincode']