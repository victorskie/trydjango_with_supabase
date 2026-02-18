from django.contrib import admin
from .models import RecipeIngredient, Recipe
from django.contrib.auth import get_user_model


User = get_user_model()
# admin.site.unregister(User)

# admin.site.register(RecipeIngredient)


# class UserInline(admin.TabularInline):
#     model = User


# class RecipeInline(admin.StackedInline):
#     model = Recipe
#     extra = 0

# class UserAdmin(admin.ModelAdmin):
#     inlines = [RecipeInline]
#     list_display = ['username']

# admin.site.register(User, UserAdmin)



class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = [ 'timestamp', 'updated']
    raw_id_fields = ['user']


admin.site.register(Recipe, RecipeAdmin)









