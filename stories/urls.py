from django.urls import path
from .views import (
    index,
    CityListView,
    CityCreateView,
    CityUpdateView,
    CityUpdateView,
    CityDeleteView,
    PublicationListView,
    PublicationDetailView,
    PublicationCreateView,
    PublicationUpdateView,
    PublicationDeleteView,
    toggle_assign_to_publication,

)


app_name = "stories"


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
    path("publications/", PublicationListView.as_view(), name="publication-list"),
    path("publications/<int:pk>/", PublicationDetailView.as_view(), name="publication-detail"),
    path("publications/create/", PublicationCreateView.as_view(), name="publication-create"),
    path("publications/<int:pk>/update/", PublicationUpdateView.as_view(), name="publication-update"),
    path("publications/<int:pk>/delete/", PublicationDeleteView.as_view(), name="publication-delete"),
    path(
        "cars/<int:pk>/toggle-assign/",
        toggle_assign_to_publication,
        name="toggle-publication-assign",
    ),
    ]
