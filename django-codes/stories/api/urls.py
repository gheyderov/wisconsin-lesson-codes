from django.urls import path
from stories.api.views import categories, recipes, recipe_update, RecipeListAPIView, RecipeUpdateDeleteAPIView

urlpatterns = [
    path('categories/', categories, name = 'categories'),
    path('recipes/', RecipeListAPIView.as_view(), name = 'recipes'),
    path('recipe/<int:pk>/', RecipeUpdateDeleteAPIView.as_view(), name = 'recipe_update')
]