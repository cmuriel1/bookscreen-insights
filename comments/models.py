from django.db import models
from django.contrib.auth.models import User 

from products.models import Product

class Comment(models.Model):
    class PRODUCT_RATING(models.TextChoices):
        ONE = 1, '1'
        TWO = 2, '2'
        THREE = 3, '3'
        FOUR = 4, '4'
        FIVE = 5, '5'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(max_length=2500)
    rating = models.CharField(max_length=5, choices=PRODUCT_RATING.choices)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:20]