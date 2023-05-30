from django.urls import path
from stories.views import (
    story, 
    recipe, 
    create_story, 
    recipe_detail, 
    like_post
    )

urlpatterns = [
    path('stories/', story, name='stories'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipes/', recipe, name='recipes'),
    path('like_post/<int:pk>/', like_post, name='like_post'),
    path('create_story/', create_story, name='create_story'),
]
