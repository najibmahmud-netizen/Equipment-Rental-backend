from django.test import TestCase
from django.contrib.auth.models import User
from equipment.models import Category, Equipment
from .models import RentalRequest


class RentalRequestTest(TestCase):

    def test_create_rental_request(self):

        user = User.objects.create_user(
            username="john",
            password="1234"
        )

        category = Category.objects.create(name="Laptop")

        equipment = Equipment.objects.create(
            category=category,
            name="HP EliteBook",
            description="Good laptop",
            daily_price=100,
            quantity=2,
            available=True
        )

        rental = RentalRequest.objects.create(
            customer=user,
            equipment=equipment,
            start_date="2026-08-01",
            end_date="2026-08-05"
        )

        self.assertEqual(rental.status, "Pending")