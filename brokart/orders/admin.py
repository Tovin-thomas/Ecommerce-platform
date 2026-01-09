from django.contrib import admin
from orders.models import Order,OrderedItem
admin.site.register(OrderedItem)

class OrderAdmin(admin.ModelAdmin):
    list_filter = [
        "owner",
        "order_status",
    ]
    search_fields = (
        "owner__name",
        "id",
    )

admin.site.register(Order, OrderAdmin)