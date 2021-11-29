from django.http import HttpResponse
from rest_framework.relations import PrimaryKeyRelatedField

from .models import User, Product, Photo, Post, Comment, Transaction
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

class PostSerializer(serializers.ModelSerializer):
    # userId = UserSerializer(many=False, read_only=False)
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comment = obj.comment_set.all()
        return CommentSerializer(instance=comment, many=True).data

    def to_representation(self, instance):
        self.fields['userId'] =  UserSerializer(read_only=True)
        return super(PostSerializer, self).to_representation(instance)

    class Meta:
        model = Post
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        self.fields['product'] = ProductSerializer(read_only=True)
        self.fields['provider'] = UserSerializer(read_only=True)
        self.fields['customer'] = UserSerializer(read_only=True)
        return super(TransactionSerializer, self).to_representation(instance)

    class Meta:
        model = Transaction
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    # userId = UserSerializer(many=False, read_only=False)
    postId = PrimaryKeyRelatedField(queryset=Post.objects.all())

    def to_representation(self, instance):
        self.fields['userId'] =  UserSerializer(read_only=True)
        return super(CommentSerializer, self).to_representation(instance)

    class Meta:
        model = Comment
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    userId = PrimaryKeyRelatedField(queryset=User.objects.all())
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.photo_set.all()
        return ProductPhotoSerializer(instance=image, many=True).data

    def create(self, validated_data):
        images = self.context['request'].FILES
        product = Product.objects.create(**validated_data)
        for image in images.getlist('image'):
            Photo.objects.create(product = product, image = image)

        return product

    class Meta:
        model = Product
        fields = '__all__'

