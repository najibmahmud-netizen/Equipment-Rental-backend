from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Equipment category such as Laptop, Camera or Projector.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    """
    Equipment available for rent.
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="equipment"
    )

    name = models.CharField(max_length=150)
    description = models.TextField()
    daily_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="equipment/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.equipment.name}"