"""This file handles the admin."""

from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline,]


class IngredientAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient)
