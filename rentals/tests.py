from django.test import TestCase
from django.contrib.auth.models import User

from equipment.models import Category, Equipment
from .models import RentalRequest


class RentalRequestTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="john",
            password="1234"
        )

        self.category = Category.objects.create(
            name="Laptop"
        )

        self.equipment = Equipment.objects.create(
            category=self.category,
            name="HP EliteBook",
            description="Good laptop",
            daily_price=100,
            quantity=2,
            available=True,
        )

    def test_create_rental_request(self):
        rental = RentalRequest.objects.create(
            customer=self.user,
            equipment=self.equipment,
            start_date="2026-08-01",
            end_date="2026-08-05",
        )

        self.assertEqual(rental.status, "Pending")
        self.assertEqual(rental.customer.username, "john")
        self.assertEqual(rental.equipment.name, "HP EliteBook")

    def test_equipment_quantity(self):
        self.assertEqual(self.equipment.quantity, 2)

    def test_equipment_is_available(self):
        self.assertTrue(self.equipment.available)

    def test_category_name(self):
        self.assertEqual(str(self.category), "Laptop")

    def test_equipment_string(self):
        self.assertEqual(str(self.equipment), "HP EliteBook")

    def test_rental_string(self):
        rental = RentalRequest.objects.create(
            customer=self.user,
            equipment=self.equipment,
            start_date="2026-08-01",
            end_date="2026-08-05",
        )

        self.assertIn("john", str(rental))