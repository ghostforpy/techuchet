import imp
from django.urls import path

from .views import ListAndCreateConnectionUnitView, UpdateConnectionUnitView



urlpatterns = [
    path("", ListAndCreateConnectionUnitView.as_view(), name='connection-list'),
    path("<int:pk>/", UpdateConnectionUnitView.as_view(), name='connection-detail'),

]