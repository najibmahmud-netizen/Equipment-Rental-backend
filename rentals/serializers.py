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

    def validate(self, data):
        equipment = data["equipment"]

        # Check dates
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError(
                "Start date cannot be after end date."
            )

        # Check equipment availability
        if not equipment.available:
            raise serializers.ValidationError(
                "This equipment is not available."
            )

        # Check quantity
        if equipment.quantity <= 0:
            raise serializers.ValidationError(
                "This equipment is out of stock."
            )

        # Prevent duplicate active requests
        user = self.context["request"].user

        duplicate = RentalRequest.objects.filter(
            customer=user,
            equipment=equipment,
            status__in=["Pending", "Approved"],
        ).exists()

        if duplicate:
            raise serializers.ValidationError(
                "You already have an active rental request for this equipment."
            )

        return data