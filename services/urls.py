import imp
from django.urls import path

from .views import ListAndCreateServiceView, UpdateServiceView, ServiceNameListView



urlpatterns = [
    path("service-names/<int:type_pk>/", ServiceNameListView.as_view(), name='servise-names'),
    path("<int:pk>/", UpdateServiceView.as_view(), name='service-detail'),
    path("", ListAndCreateServiceView.as_view(), name='service-list'),


]