from typing import Any, Dict
from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'content',
        )
        widgets = {
            'content' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your message'
            }),
        }


class RecipeCreateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = (
            'title',
            'image',
            'cover_image',
            'small_description',
            'description',
            'category',
            'tags'
        )
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Title'
            }),
            'image' : forms.FileInput,
            'cover_image' : forms.FileInput,
            'small_description' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Small Description'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Description'
            }),
            'category' : forms.Select(attrs={
                'class' : 'form-control',
            }),
            'tags' : forms.SelectMultiple(attrs={
                'class' : 'form-control',
            }),
            
        }
