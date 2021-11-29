from django.db import models

# Create your models here.
from django.utils import timezone
### Board


class User(models.Model):
    nickname = models.CharField(max_length=30)

class Post(models.Model):
    content = models.TextField(max_length=100)
    userId = models.ForeignKey("User", on_delete=models.CASCADE, db_column='userId')

class Comment(models.Model):
    content = models.CharField(max_length=1000)
    postId = models.ForeignKey("Post", on_delete=models.CASCADE, db_column='postId')
    userId = models.ForeignKey("User", on_delete=models.CASCADE, db_column='userId')

class Product(models.Model):
    brand = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    price = models.BigIntegerField(default=0)
    quality = models.TextField(max_length=50)
    description = models.TextField(max_length=1000, default="")
    rentAvailableStartDate = models.DateField(default=timezone.now())
    rentAvailableEndDate = models.DateField(default=timezone.now())
    directAvailable = models.BooleanField(default=False)
    isEscrow = models.BooleanField(default=False)
    lat = models.DecimalField(max_digits=20, decimal_places=10)
    lng = models.DecimalField(max_digits=20, decimal_places=10)
    category = models.TextField(max_length=50)
    transaction = models.TextField(max_length=50)
    createdAt = models.DateField(default=timezone.now())
    userId = models.ForeignKey("User", on_delete=models.CASCADE, db_column='userId')

class Transaction(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, db_column="product", related_name="productId")
    provider = models.ForeignKey(User, on_delete=models.CASCADE, db_column="provider", related_name="providerId")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, db_column="customer", related_name="customerId")
    totalBalance = models.IntegerField(default=0)
    type = models.CharField(max_length=100)
    rentStartDate = models.DateField(default=timezone.now())
    rentEndDate = models.DateField(default=timezone.now())
    confirmation = models.BooleanField(default=False)

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='productImages/', blank=True, null=True)
