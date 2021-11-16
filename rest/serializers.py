from rest_framework.relations import PrimaryKeyRelatedField

from .models import User, Product, Photo
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname']


class ProductPhotoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Photo
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    userId = PrimaryKeyRelatedField(read_only=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.photo_set.all()
        return ProductPhotoSerializer(instance=image, many=True).data

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
                  'userId',
                  'images']
