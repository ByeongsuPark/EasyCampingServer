from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, ProductSerializer, PostSerializer, CommentSerializer, TransactionSerializer
from .models import User, Product, Post, Comment, Transaction
from django.shortcuts import render, get_object_or_404


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_objects(self):
        return get_object_or_404(User, id=self.request.query_params.get('id'))

    def get_queryset(self):
        return User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get_object(self):
        return get_object_or_404(Product, id=self.request.query_params.get('id'))

    def get_queryset(self):
        return Product.objects.all()

    def retrieve(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    lookup_field = 'id'

    def get_object(self):
        return get_object_or_404(Post, id=self.request.query_params.get('id'))

    def get_queryset(self):
        return Post.objects.all()

    def retrieve(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        serializer = PostSerializer(post)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_object(self):
        return get_object_or_404(Comment, id=self.request.query_params.get('id'))

    def get_queryset(self):
        return Comment.objects.all()

    def retrieve(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    lookup_field = 'id'

    def get_object(self):
        return get_object_or_404(Transaction)

    def get_queryset(self):
        return Transaction.objects.all()

    def retrieve(self, request, *args, **kwargs):
        transaction = get_object_or_404(Transaction, pk=self.kwargs.get('pk'))
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def retrieve_by_user(self, request, *args, **kwargs):
        transaction = Transaction.objects.filter(customer_id=self.kwargs.get('id'))
            # get_object_or_404(Transaction, customer_id=self.kwargs.get('id'))
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)



