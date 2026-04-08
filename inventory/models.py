from django.conf import settings
from django.db import models

from meals.signals import meal_added, meal_removed
from meals.utils import generate_meal_queue_totals

User = settings.AUTH_USER_MODEL

class InventoryRequestStatus(models.TextChoices):
    REQUESTED = 'r', 'Requested'
    PURCHASED = 'p', 'Purchased'
    STOCKED = 's', 'In Stock'
    UNAVAILABLE = 'u', 'Unavailable'
    DECLINED = 'd', 'Declined'
    ARCHIVED = 'a', 'Archive'

class InventoryRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    unit = models.CharField(max_length=50, blank=True, null=True)
    total = models.DecimalField(decimal_places=4, max_digits=20, blank=True, null=True)
    status = models.CharField(max_length=1, choices=InventoryRequestStatus.choices, default=InventoryRequestStatus.REQUESTED)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


# --- SIGNAL RECEIVER ---
def meal_queue_update_receiver(sender, user, *args, **kwargs):
    # 1. Find all active grocery lists for this user and archive them
    qs = InventoryRequest.objects.filter(user=user, status=InventoryRequestStatus.REQUESTED)
    if qs.exists():
        qs.update(status=InventoryRequestStatus.ARCHIVED)
    
    # 2. Generate the fresh, math-calculated totals
    data = generate_meal_queue_totals(user)
    
    # 3. Loop through our calculated dictionary and convert them into database objects
    inventory_items = []
    for item in data:
        inventory_items.append(
            InventoryRequest(
                user=user,
                name=item['name'],
                unit=item['unit'],
                total=item['quantity'] 
            )
        )
        
    # 4. Save all the new ingredients to the database instantly
    InventoryRequest.objects.bulk_create(inventory_items)

# Connect the signals manually
meal_added.connect(meal_queue_update_receiver)
meal_removed.connect(meal_queue_update_receiver)
