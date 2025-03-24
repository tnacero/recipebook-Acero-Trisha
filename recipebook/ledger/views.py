"""This file handles the views."""

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm
# Create your views here.


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe_detail.html"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_create.html'

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipeimage_create.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        ctx['recipe'] = Recipe.objects.get(pk=pk)
        ctx['form'] = RecipeImageForm()
        return ctx
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        form = RecipeImageForm(request.POST, request.FILES)

        if (form.is_valid()):
            ri = RecipeImage()
            ri.image = request.FILES.get('image')
            ri.description = request.POST.get('description')
            ri.recipe = Recipe.objects.get(pk=pk)

            ri.save()

            return redirect(reverse('ledger:recipe-detail', args=[pk]))
        
        else:
            self.object_list = self.get_queryset()
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        