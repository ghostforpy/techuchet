import imp
from django.urls import path

from .views import ListAndCreateConnectionUnitView, UpdateConnectionUnitView, create_connection_units



urlpatterns = [
    path("", ListAndCreateConnectionUnitView.as_view(), name='connection-list'),
    path("<int:pk>/", UpdateConnectionUnitView.as_view(), name='connection-detail'),
    path("create_connection_units/", create_connection_units, name="create_connection_units")
]