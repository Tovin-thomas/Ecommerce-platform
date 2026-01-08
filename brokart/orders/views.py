from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from products.models import Product
from customers.models import Customer

# Create your views here.
def showcart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context = {'cart': cart_obj}
    return render(request, 'cart.html', context)

def add_to_cart(request):
    if request.method == "POST":
        user = request.user
        customer=user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)

        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        
        # Try to get or create the item, handling potential duplicates from previous code
        try:
            ordered_item, created = OrderedItem.objects.get_or_create(
                product=product,
                owner=cart_obj
            )
            if created:
                ordered_item.quantity = quantity
            else:
                ordered_item.quantity += quantity
            ordered_item.save()
        except OrderedItem.MultipleObjectsReturned:
            # If duplicates exist, merge them into one and delete others
            items = OrderedItem.objects.filter(product=product, owner=cart_obj)
            ordered_item = items.first()
            # Calculate total quantity from all duplicates
            total_qty = sum(item.quantity for item in items) + quantity
            ordered_item.quantity = total_qty
            ordered_item.save()
            # Delete the other duplicates
            items.exclude(id=ordered_item.id).delete()

        return redirect('cart')
    


    
    


