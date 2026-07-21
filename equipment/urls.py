from django.urls import path

from .views import (
    CategoryListView,
    EquipmentListCreateView,
    EquipmentDetailView,
    ReviewListCreateView,
)

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="categories"),

    path("", EquipmentListCreateView.as_view(), name="equipment-list"),

    path("<int:pk>/", EquipmentDetailView.as_view(), name="equipment-detail"),

    path("reviews/", ReviewListCreateView.as_view(), name="reviews"),
]