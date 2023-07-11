from stories.models import Category, Recipe
from django.http import JsonResponse
from stories.api.serializers import (
    CategorySerializer, 
    RecipeSerializer, 
    RecipeCreateSerializer
    )
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

def categories(request):
    category_list = Category.objects.all()
    # category_dict = []
    # for category in category_list:
    #     category_dict.append({
    #         'cat_id' : category.id,
    #         'cat_title': category.title
    #     })
    serializer = CategorySerializer(category_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)


@api_view(http_method_names=['GET', 'POST'])
def recipes(request):
    if request.method == 'POST':
        serializer = RecipeCreateSerializer(data = request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe = False, status = 201)
        return JsonResponse(data=serializer.errors, safe = False, status = 400)
    recipe_lists = Recipe.objects.all()
    serializer = RecipeSerializer(recipe_lists, context = {'request':request}, many = True)
    return JsonResponse(data=serializer.data, safe = False)


@api_view(http_method_names=['PUT', 'PATCH'])
def recipe_update(request, pk):
    recipe = Recipe.objects.get(id = pk)
    if request.method == 'PUT':
        serializer = RecipeCreateSerializer(data = request.data, context = {'request':request}, instance = recipe)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe = False, status = 201)
        return JsonResponse(data=serializer.errors, safe = False, status = 400)
    if request.method == 'PATCH':
        serializer = RecipeCreateSerializer(data = request.data, partial = True, context = {'request':request}, instance = recipe)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe = False, status = 201)
        return JsonResponse(data=serializer.errors, safe = False, status = 400)
    

class RecipeListAPIView(ListCreateAPIView):
    # serializer_class = RecipeCreateSerializer
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecipeSerializer
        return RecipeCreateSerializer
    

class RecipeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeCreateSerializer
    queryset = Recipe.objects.all()

