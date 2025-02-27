"""This file handles the admin."""

from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeIngredient, Ingredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]


class IngredientAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient)
