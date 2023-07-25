from django.urls import path
from stories.api.views import categories, TagListAPIView, recipe_update, RecipeListAPIView, RecipeUpdateDeleteAPIView, SubscriberCreateAPIView

urlpatterns = [
    path('categories/', categories, name = 'categories'),
    path('subscribers/', SubscriberCreateAPIView.as_view(), name = 'subscribers'),
    path('tags/', TagListAPIView.as_view(), name = 'tags'),
    path('recipes/', RecipeListAPIView.as_view(), name = 'recipes_lists'),
    path('recipe/<int:pk>/', RecipeUpdateDeleteAPIView.as_view(), name = 'recipe_update')
]