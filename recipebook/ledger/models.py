from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient', args=[str(self.name)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.name)])
    
class RecipeIngredient(models.Model):
    quantity = models.IntegerField
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL,related_name="ingredients")
