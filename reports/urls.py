from django.urls import path
from django.views.generic import TemplateView

from .views import abonents_report



urlpatterns = [
    path("", TemplateView.as_view(template_name="reports/main.html"), name="reports-main"),
    path("abonents_report", abonents_report, name="abonents-report")
]