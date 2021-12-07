import django_tables2 as tables
from .models import Orderdata
from myapp.models import Order


class PersonTable(tables.Table):
    CancleOrder = tables.TemplateColumn(template_name='delete_icon.html')
    model_name = tables.Column(accessor='product.model_name')
    price = tables.Column(accessor='product.price')
    totalprice = tables.Column(accessor='price',verbose_name="Total Price")
    

   
    class Meta:
            model = Orderdata
            template_name = "django_tables2/bootstrap-responsive.html"
            fields = ("model_name","price","totalprice")

