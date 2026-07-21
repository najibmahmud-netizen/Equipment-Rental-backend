from django.urls import path
from .views import (
    RentalRequestListCreateView,
    AllRentalRequestsView,
)

urlpatterns = [
    path("", RentalRequestListCreateView.as_view(), name="my-rentals"),
    path("all/", AllRentalRequestsView.as_view(), name="all-rentals"),
]