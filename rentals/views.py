from rest_framework import generics, permissions
from .models import RentalRequest
from .serializers import RentalRequestSerializer


class RentalRequestListCreateView(generics.ListCreateAPIView):
    """
    Customers can:
    - View their rental requests
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