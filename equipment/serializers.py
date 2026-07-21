from rest_framework import serializers
from .models import Category, Equipment, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Equipment
        fields = [
            "id",
            "name",
            "category",
            "category_name",
            "description",
            "daily_price",
            "quantity",
            "available",
            "image",
            "created_at",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source="customer.username")

    class Meta:
        model = Review
        fields = [
            "id",
            "customer",
            "customer_name",
            "equipment",
            "rating",
            "comment",
            "created_at",
        ]