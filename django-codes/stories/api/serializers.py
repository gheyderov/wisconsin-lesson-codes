from rest_framework import serializers
from stories.models import Category, Recipe, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title'
        )


class RecipeSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source = 'category.title')
    category = CategorySerializer()
    tags = TagSerializer(many = True)
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'category',
            'tags',
            'author_name',
            'small_description',
            'description',
            'image',
            'cover_image'
        )


class RecipeCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only = True)
    author = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'category',
            'tags',
            'author',
            'slug',
            'small_description',
            'description',
            'image',
            'cover_image'
        )

    def validate(self, attrs):
        request = self.context['request']
        attrs['author'] = request.user
        return super().validate(attrs)




