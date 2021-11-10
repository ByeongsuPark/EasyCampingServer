from django.contrib import admin
from .models import User, Product, Photo


# PHOTO 클래스를 INLINE으로 나타냄
class PhotoInline(admin.TabularInline):
    model = Photo


# Product 클래스로 해당하는 photo 객체 리스트로 관리
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]


# Register your models here.

admin.site.register(User)
admin.site.register(Product, ProductAdmin)

