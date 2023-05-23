from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category, Tag

# Create your views here.

def story(request):
    return render(request, 'stories.html')


def recipe(request):
    recipes = Recipe.objects.all()
    context = {
        'recipe_lists' : recipes,
    }
    return render(request, 'recipes.html', context)

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, id = pk)
    tags = Tag.objects.all()
    context = {
        'recipe' : recipe,
        'tags' : tags
    }
    return render(request, 'single.html', context)

def create_story(request):
    return render(request, 'create_story.html')