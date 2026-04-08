from django.contrib.auth import get_user_model

User = get_user_model()

def generate_meal_queue_totals(user):
    # We import Meal here locally to avoid circular import errors
    from .models import Meal
    from recipes.models import RecipeIngredient
    
    # 1. Fetch all pending meals for this specific user
    pending_meals = Meal.objects.by_user(user).pending()
    
    # 2. Grab all the unique recipe IDs from those meals
    recipe_ids = pending_meals.values_list('recipe_id', flat=True)
    
    # 3. Fetch all ingredients that belong to those specific recipes
    ingredients = RecipeIngredient.objects.filter(recipe_id__in=recipe_ids)
    
    # 4. Group and sum them up into a dictionary
    totals = {}
    for item in ingredients:
        # Clean up the text so "Chicken" and "chicken " group together properly
        name = item.name.lower().strip() if item.name else "unknown"
        unit = item.unit.lower().strip() if item.unit else ""
        
        # Create a unique key for grouping (e.g., "chicken_pound")
        key = f"{name}_{unit}"
        
        if key not in totals:
            totals[key] = {
                "name": name,
                "unit": unit,
                "quantity": 0
            }
        
        # Add the floating point quantities together
        if item.quantity_as_float:
            totals[key]["quantity"] += item.quantity_as_float
            
    # Return a clean list of the aggregated ingredients
    return list(totals.values())