from django.db import models

# Create your models here.
from django.utils import timezone


class User(models.Model):
    nickname = models.CharField(max_length=30)


class Product(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.BigIntegerField(default=0)
    quality = models.CharField(max_length=50)
    rentAvailableStartDate = models.DateField(default=timezone.now())
    rentAvailableEndDate = models.DateField(default=timezone.now())
    directAvailable = models.BooleanField(default=False)
    isEscrow = models.BooleanField(default=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    category = models.CharField(max_length=50)
    transaction = models.CharField(max_length=50)
    createdAt = models.DateField(default=timezone.now())
    userId = models.ForeignKey("User", on_delete=models.CASCADE, db_column='userId')


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='productImages/', blank=True, null=True)
