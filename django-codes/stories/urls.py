from django.urls import path
from stories.views import story, recipe, create_story, recipe_detail

urlpatterns = [
    path('stories/', story, name='stories'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipes/', recipe, name='recipes'),
    path('create_story/', create_story, name='create_story'),
]
