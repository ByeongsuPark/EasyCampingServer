"""EasyCampingServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from rest.views import UserViewSet, ProductViewSet, PostViewSet, CommentViewSet, TransactionViewSet

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/user/', UserViewSet.as_view({
                      'get': 'list',
                  })),
                  path('api/product/', ProductViewSet.as_view({
                      'get': 'list',
                      'post': 'create',
                  })),
                  path('api/product/<int:pk>/', ProductViewSet.as_view({
                      'get': 'retrieve',
                  })),
                  path('api/user/<int:pk>/', UserViewSet.as_view({
                      'get': 'retrieve',
                  })),
                  path('api/post/', PostViewSet.as_view({
                      'get': 'list',
                      'post': 'create',
                  })),
                  path('api/post/<int:pk>/', PostViewSet.as_view({
                      'get': 'retrieve',
                  })),
                  path('api/comment/', CommentViewSet.as_view({
                      'get': 'list',
                      'post': 'create',
                  })),
                  path('api/comment/<int:pk>/', CommentViewSet.as_view({
                      'get': 'retrieve',
                  })),
                  path('api/transaction/', TransactionViewSet.as_view({
                      'get': 'list',
                      'post': 'create',
                  })),
                  path('api/transaction/user/<int:id>', TransactionViewSet.as_view({
                      'get': 'retrieve_by_user',
                  })),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
