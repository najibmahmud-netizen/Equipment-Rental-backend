from django.urls import path

from .views import (
    RentalRequestListCreateView,
    AllRentalRequestsView,
    ApproveRentalView,
    RejectRentalView,
    ReturnRentalView,
)

urlpatterns = [
    path("", RentalRequestListCreateView.as_view(), name="my-rentals"),
    path("all/", AllRentalRequestsView.as_view(), name="all-rentals"),
    path("<int:pk>/approve/", ApproveRentalView.as_view(), name="approve-rental"),
    path("<int:pk>/reject/", RejectRentalView.as_view(), name="reject-rental"),
    path("<int:pk>/return/", ReturnRentalView.as_view(), name="return-rental"),
]