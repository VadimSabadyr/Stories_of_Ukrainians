from django.urls import path
from .views import (
    index,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "cities/",
        CityListView.as_view(),
        name="city-list",
    ),
    path(
        "cities/create/",
        CityCreateView.as_view(),
        name="city-create",
    ),
    path(
        "cities/<int:pk>/update/",
        CityUpdateView.as_view(),
        name="city-update",
    ),
    path(
        "cities/<int:pk>/delete/",
        CityDeleteView.as_view(),
        name="city-delete",
    ),
    ]
