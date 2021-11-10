from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, ProductSerializer
from .models import User, Product
from django.shortcuts import render, get_object_or_404


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_objects(self):
        return get_object_or_404(User, id=self.request.query_params.get('id'))

    def get_queryset(self):
        return User.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_object(self):
        return get_object_or_404(Product, id=self.request.query_params.get('id'))

    def get_queryset(self):
        return Product.objects.all()
