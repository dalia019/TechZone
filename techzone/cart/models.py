from django.db import models
from django.contrib.auth.models import User
from products.models import Product  # تأكد إنك عامل app اسمه products وفيه Product

class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.customer.username} - {self.product.name} x {self.quantity}"

class Wishlist(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.username} ❤ {self.product.name}"

