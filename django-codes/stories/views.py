from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Recipe, Category, Tag
from django.contrib import messages


# Create your views here.

def story(request):
    return render(request, 'stories.html')


def recipe(request):
    print('Liked posts: ', request.session.get('liked_posts'))
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

# def like_post(request, pk):
#     request.session['liked_posts'] = request.session.get('liked_posts', ' ') + str(pk) + ' '
#     messages.add_message(request, messages.SUCCESS, "Liked")
#     return render(request, 'recipes.html')

def like_post(request, pk):
    response = HttpResponse('test')
    response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', ' ') + str(pk) + ' ')
    return response