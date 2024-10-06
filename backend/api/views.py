from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import CategorySerializer,ProductSerializer
from store.models import Category,Product
from api.permissions import IsAdminOrSuperUser

# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAdminOrSuperUser]


class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAdminOrSuperUser]

