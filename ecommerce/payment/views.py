from django.shortcuts import render,redirect
from myapp.models import Order,Product
from django.contrib import messages
from . serializer import *
from .tables import PersonTable
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView

# Create your views here.
def payment(request):
    user=request.user
    print(user,"iiiii")
    order_data=Order.objects.filter(user__username=user)
    print(order_data,"kkkkk")

    for i in order_data:
        name=i.first_name
        print(name)
    
    print(name,"na,mm")
    return render(request,"payment.html",{"name":name})

def paynow(request):
    user=request.user
    print(user.id)

    order_data=Order.objects.filter(user__username=user).first()

    price=order_data.price
    product=Product.objects.get(pk=order_data.product_id)
    print(product)
    
    if request.method=="POST":
       transection_id = create_transection_id()
       print(transection_id,"ttttt")
    
       data = {
           "orderid": order_data.id,
           "user": user.id,
           "transection_id": transection_id,
           "price": price,
           "product": product.id,
       }
       serializers = OrderdataSerializer(data=data)
       print(serializers)
    
       if serializers.is_valid():
            serializers.save()
            messages.success(request ,f"payment of Rs"+str(price)+".00 to Motorcar Suceeded. Your transaction id is : "+ str(transection_id)+".")
            return redirect('successfulpayment')
    return render(request,"paynow.html",{"data":data})
    # return render(request,"paynow.html")

def create_transection_id():  # create 
    import random
    random_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    transection_id = ''.join(random.sample(random_string, 15))
    return transection_id

def successpayment(request):
    return render(request,"successfulpayment.html")

def order(request):
    user=request.user
    print(user)
    order_summary=Orderdata.objects.filter(user=user.id)
    table_data=PersonTable(order_summary)

    for i in order_summary:
        print(i.price,"pppppppyyyyy")#total price orderdata
        print(i.orderid.price)
        print(i.product.model_name)
    
    return render(request,"order.html",{"table_data":table_data})

class OrderDeleteView(DeleteView):
    model = Orderdata
    success_url = reverse_lazy('getorders')

    def post(self, request, *args, **kwargs):
        if "delete" in request.POST:
            print("oooiioio")
            order_data=Orderdata.objects.filter(user=request.user)
            # print(order_data.price,"ppp999999")
            print(order_data)
            loss=0
            for i in order_data:
                loss=(i.price*10)/100
                d_price=i.price-loss
                print(d_price,"ppppp")
                
            messages.success(request ,f"Your order cancellation is Succeed "+str(d_price)+".00 to Refund")
            # return redirect('successfulpayment')
            return super(OrderDeleteView, self).post(request, *args, **kwargs) 
        else:
            return redirect('getorders')