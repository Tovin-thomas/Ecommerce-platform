import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brokart.settings')
django.setup()

from orders.models import OrderedItem

def cleanup():
    items = OrderedItem.objects.all()
    print(f"Current OrderedItems count: {items.count()}")
    for item in items:
        print(f"ID: {item.id}, Product: {item.product}, Cart: {item.owner_id}, Quantity: {item.quantity}")
    
    # Delete all
    count, _ = items.delete()
    print(f"Deleted {count} items.")
    print(f"Remaining OrderedItems count: {OrderedItem.objects.count()}")

if __name__ == "__main__":
    cleanup()
