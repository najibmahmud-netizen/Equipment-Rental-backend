from django.db import models
from django.contrib.auth.models import User
from equipment.models import Equipment


class RentalRequest(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Returned", "Returned"),
    ]

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rental_requests"
    )

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name="rental_requests"
    )

    request_date = models.DateTimeField(auto_now_add=True)

    start_date = models.DateField()

    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    returned_at = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.customer.username} - {self.equipment.name}"