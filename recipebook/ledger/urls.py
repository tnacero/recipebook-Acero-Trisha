from django.urls import path 
from .views import recipes_list, recipe_one, recipe_two, RecipesList

urlpatterns = [
    path('recipes/list', RecipesList.as_view(), name='recipes-list'),
    path('recipe/1', recipe_one, name='recipe-1'),
    path('recipe/2', recipe_two, name='recipe-2'),
]

app_name = 'ledger'