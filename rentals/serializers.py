from rest_framework import serializers
from .models import RentalRequest


class RentalRequestSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source="customer.username")
    equipment_name = serializers.ReadOnlyField(source="equipment.name")

    class Meta:
        model = RentalRequest
        fields = [
            "id",
            "customer",
            "customer_name",
            "equipment",
            "equipment_name",
            "request_date",
            "start_date",
            "end_date",
            "status",
            "returned_at",
        ]

        read_only_fields = [
            "customer",
            "request_date",
            "status",
            "returned_at",
        ]