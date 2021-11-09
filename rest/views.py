from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from django.shortcuts import render, get_object_or_404
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_objects(self):
        return get_object_or_404(User, id=self.request.query_params.get('id'))

    def get_queryset(self):
        return User.objects.all()