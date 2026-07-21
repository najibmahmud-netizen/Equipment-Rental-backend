from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RentalRequest
from .serializers import RentalRequestSerializer


class RentalRequestListCreateView(generics.ListCreateAPIView):
    """
    Customers can:
    - View their own rental requests
    - Create a new rental request
    """
    serializer_class = RentalRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RentalRequest.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class AllRentalRequestsView(generics.ListAPIView):
    """
    Admin can view all rental requests.
    """
    queryset = RentalRequest.objects.all()
    serializer_class = RentalRequestSerializer
    permission_classes = [permissions.IsAdminUser]


class ApproveRentalView(APIView):
    """
    Admin approves a rental request.
    """
    permission_classes = [permissions.IsAdminUser]

    def patch(self, request, pk):
        rental = get_object_or_404(RentalRequest, pk=pk)

        equipment = rental.equipment

        if equipment.quantity <= 0:
            return Response(
                {"error": "Equipment is out of stock."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        rental.status = "Approved"
        rental.save()

        equipment.quantity -= 1

        if equipment.quantity == 0:
            equipment.available = False

        equipment.save()

        return Response(
            {"message": "Rental approved successfully."},
            status=status.HTTP_200_OK
        )


class RejectRentalView(APIView):
    """
    Admin rejects a rental request.
    """
    permission_classes = [permissions.IsAdminUser]

    def patch(self, request, pk):
        rental = get_object_or_404(RentalRequest, pk=pk)

        rental.status = "Rejected"
        rental.save()

        return Response(
            {"message": "Rental rejected successfully."},
            status=status.HTTP_200_OK
        )


class ReturnRentalView(APIView):
    """
    Admin marks equipment as returned.
    """
    permission_classes = [permissions.IsAdminUser]

    def patch(self, request, pk):
        rental = get_object_or_404(RentalRequest, pk=pk)

        rental.status = "Returned"
        rental.returned_at = timezone.now()
        rental.save()

        equipment = rental.equipment
        equipment.quantity += 1
        equipment.available = True
        equipment.save()

        return Response(
            {"message": "Equipment returned successfully."},
            status=status.HTTP_200_OK
        )