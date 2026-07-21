from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticated,
)

from .models import Category, Equipment, Review
from .serializers import (
    CategorySerializer,
    EquipmentSerializer,
    ReviewSerializer,
)


class CategoryListView(generics.ListAPIView):
    """
    Return all equipment categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class EquipmentListCreateView(generics.ListCreateAPIView):
    """
    GET  -> List all equipment
    POST -> Add new equipment (Admin only)
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    -> Equipment details
    PUT    -> Update equipment
    DELETE -> Delete equipment
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class ReviewListCreateView(generics.ListCreateAPIView):
    """
    GET  -> List all reviews
    POST -> Create a review
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)