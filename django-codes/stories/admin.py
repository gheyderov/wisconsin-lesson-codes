from django.contrib import admin
from .models import (
    Recipe,
    Category,
    Tag,
    RecipeReview,
    Property,
    PropertyValue
)

# Register your models here.

class RecipeInlineAdmin(admin.TabularInline):
    model = RecipeReview

admin.site.register(Tag)
admin.site.register(Property)

admin.site.register(RecipeReview)

@admin.register(PropertyValue)
class PropertyValueAdmin(admin.ModelAdmin):
    list_display = ['name', 'property']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_editable = ['title']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeInlineAdmin,)
    list_display = ['title', 'category', 'author']
    list_editable = ['category']
    list_filter = ['category', 'author']

