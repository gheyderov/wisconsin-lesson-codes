from django.urls import path
from stories.views import (
    story, 
    RecipeListView, 
    create_story, 
    RecipeDetailView, 
    like_post
    )

urlpatterns = [
    path('stories/', story, name='stories'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('like_post/<int:pk>/', like_post, name='like_post'),
    path('create_story/', create_story, name='create_story'),
]
