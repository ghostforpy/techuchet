import imp
from django.urls import path

from .views import ListAndCreateAbonentView, UpdateAbonentView



urlpatterns = [
    path("", ListAndCreateAbonentView.as_view(), name='abonent-list'),
    path("<int:pk>/", UpdateAbonentView.as_view(), name='abonent-detail'),
]