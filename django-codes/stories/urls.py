from django.urls import path
from stories.views import (
    story, 
    RecipeListView, 
    create_story, 
    RecipeDetailView, 
    like_post,
    CreateRecipeView,
    UpdateRecipeView
    )

urlpatterns = [
    path('stories/', story, name='stories'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('like_post/<int:pk>/', like_post, name='like_post'),
    path('create_story/', CreateRecipeView.as_view(), name='create_story'),
    path('update_story/<int:pk>/', UpdateRecipeView.as_view(), name='update_story'),
]
