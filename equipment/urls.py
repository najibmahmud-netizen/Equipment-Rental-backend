from django.urls import path

from .views import (
    CategoryListView,
    EquipmentListCreateView,
    EquipmentDetailView,
)

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("", EquipmentListCreateView.as_view(), name="equipment-list"),
    path("<int:pk>/", EquipmentDetailView.as_view(), name="equipment-detail"),
]