import imp
from django.urls import path

from .views import ListAndCreateNodeView, UpdateNodeView



urlpatterns = [
    path("", ListAndCreateNodeView.as_view(), name='node-list'),
    path("<int:pk>/", UpdateNodeView.as_view(), name='node-detail'),

]