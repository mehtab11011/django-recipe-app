from django.contrib import admin
from .models import recipe_model
@admin.register(recipe_model)
class recipe_admin(admin.ModelAdmin):
    list_display=["recipe_name","description","image"]
# Register your models here.
