from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Category, Equipment
from .serializers import CategorySerializer, EquipmentSerializer


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