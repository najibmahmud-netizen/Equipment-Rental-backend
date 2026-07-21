from django.test import TestCase
from .models import Category


class CategoryModelTest(TestCase):

    def test_create_category(self):
        category = Category.objects.create(name="Laptop")

        self.assertEqual(category.name, "Laptop")