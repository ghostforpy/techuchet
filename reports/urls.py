import imp
from django.urls import path
from django.views.generic import TemplateView

# from .views import ListAndCreateNodeView, UpdateNodeView



urlpatterns = [
    path("", TemplateView.as_view(template_name="reports/main.html"), name="reports-main"),
]