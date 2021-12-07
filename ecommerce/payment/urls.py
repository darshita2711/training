from django.urls import path
from rest_framework import views
from . import views 
from.views import OrderDeleteView

urlpatterns=[
    path('paymentdata/',views.payment,name="paymentdata"),
    path('paymentnow/',views.paynow,name="paynow"),
    path('successfulpayment/',views.successpayment,name="successfulpayment"),
    path('order/',views.order,name="getorders"),
    path('<str:pk>/delete',OrderDeleteView.as_view(),name="cancelorder"),
]