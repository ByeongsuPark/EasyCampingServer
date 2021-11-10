from rest_framework.relations import PrimaryKeyRelatedField

from .models import User, Product
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname']


class ProductSerializer(serializers.ModelSerializer):
    userId = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['id',
                  'brand',
                  'name',
                  'price',
                  'quality',
                  'rentAvailableStartDate',
                  'rentAvailableEndDate',
                  'directAvailable',
                  'lat',
                  'lng',
                  'category',
                  'transaction',
                  'createdAt',
                  'userId']
