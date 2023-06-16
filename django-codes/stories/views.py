from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Recipe, Category, Tag
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from core.forms import CommentForm
from stories.forms import RecipeCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def story(request):
    return render(request, 'stories.html')


class RecipeListView(ListView):
    template_name = 'recipes.html'
    model = Recipe
    context_object_name = 'recipes'
    ordering = ['-created_at']
    paginate_by = 2

    def get_queryset(self) -> QuerySet[Any]:
        cat_id = self.request.GET.get('category')
        tag_id = self.request.GET.get('tag')
        queryset = super().get_queryset()
        if tag_id:
            queryset = queryset.filter(tags__id = tag_id)
        if cat_id:
            queryset = queryset.filter(category__id = cat_id)
        return queryset


def recipe(request):
    # print('Liked posts: ', request.session.get('liked_posts'))
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


class RecipeDetailView(FormMixin, DetailView):
    template_name = 'single.html'
    model = Recipe
    form_class = CommentForm
    
    def get_success_url(self) -> str:
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.recipe = self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


def create_story(request):
    return render(request, 'create_story.html')


class CreateRecipeView(LoginRequiredMixin, CreateView):
    template_name = 'create_story.html'
    form_class = RecipeCreateForm
    # success_url = reverse_lazy('home')

    # def get_success_url(self, **kwargs) -> str:
    #     return reverse_lazy('recipe_detail', kwargs = {'pk', self.get_object.})

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class UpdateRecipeView(LoginRequiredMixin, UpdateView):
    template_name = 'create_story.html'
    form_class = RecipeCreateForm
    model = Recipe


    

# def like_post(request, pk):
#     request.session['liked_posts'] = request.session.get('liked_posts', ' ') + str(pk) + ' '
#     messages.add_message(request, messages.SUCCESS, "Liked")
#     return render(request, 'recipes.html')

def like_post(request, pk):
    response = HttpResponse('test')
    response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', ' ') + str(pk) + ' ')
    return response