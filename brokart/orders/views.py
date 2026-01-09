from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Order,OrderedItem
from products.models import Product
from customers.models import Customer
from django.contrib import messages

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
    

def remove_item_from_cart(request,pk):
    item = OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')
    
def checkout_cart(request):
    if request.method == "POST":
        try:
            user = request.user
            customer=user.customer_profile
            total = float(request.POST.get('total'))

            order_obj= Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            order_obj.order_status = Order.ORDER_CONFIRMED
            order_obj.total_price = total
            order_obj.save()
            messages.success(request, 'Order is processed')
        except Exception as e:
            messages.error(request, 'Order is not processed')
    else:
        messages.error(request, 'Order is not processed')
    return redirect('cart')
@login_required(login_url='account')
def showorders(request):
    user = request.user
    customer = user.customer_profile
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}
    return render(request, 'orders.html', context)
