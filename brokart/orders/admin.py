from django.contrib import admin
from orders.models import Order,OrderedItem
admin.site.register(Order)
admin.site.register(OrderedItem)
# Register your models here.
