from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Recipe(AbstractModel):
    category = models.ForeignKey('Category', related_name='recipes', on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField('Tag')
    property_values = models.ManyToManyField('PropertyValue')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField('title', max_length=100)
    image = models.ImageField('image', upload_to='recipe/')
    cover_image = models.ImageField('cover_image', upload_to='recipe/')
    small_description = models.CharField('small_description', max_length=155)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = '-created_at',


class Property(AbstractModel):
    name = models.CharField('name', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class PropertyValue(AbstractModel):
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='values')
    name = models.CharField('name', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Property Value'
        verbose_name_plural = 'Property Values'


class RecipeReview(AbstractModel):
    message = models.CharField('message', max_length=255)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self) -> str:
        return self.recipe.title



class Category(AbstractModel):
    title = models.CharField('title', max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class Tag(AbstractModel):
    title = models.CharField('title', max_length=100)

    def __str__(self):
        return self.title