from django.urls import path
from stories.views import story, single, recipe, create_story

urlpatterns = [
    path('stories/', story, name='stories'),
    path('single/', single, name='single'),
    path('recipes/', recipe, name='recipes'),
    path('create_story/', create_story, name='create_story'),


]
