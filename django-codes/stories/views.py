from django.shortcuts import render
from .models import Recipe, Category

# Create your views here.

def story(request):
    return render(request, 'stories.html')

def single(request):
    return render(request, 'single.html')

def recipe(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    context = {
        'recipe_lists' : recipes,
        'categories' : categories

    }
    return render(request, 'recipes.html', context)

def create_story(request):
    return render(request, 'create_story.html')