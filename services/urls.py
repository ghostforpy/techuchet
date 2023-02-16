import imp
from django.urls import path

from .views import ListAndCreateServiceView, UpdateServiceView



urlpatterns = [
    path("", ListAndCreateServiceView.as_view(), name='service-list'),
    path("<int:pk>/", UpdateServiceView.as_view(), name='service-detail'),

]