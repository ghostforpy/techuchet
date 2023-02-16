# from django.shortcuts import render
# from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView

from .models import Service



# class ServiceListView(ListView):
#     model = Service
#     template_name = "services/list.html"
#     context_object_name = 'services'


class ListAndCreateServiceView(CreateView):
    model = Service
    template_name = "services/list.html"
    fields = ['name', 'type', 'abonent']
    success_url = '/services/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = self.model.objects.all()
        return context


class UpdateServiceView(UpdateView):
    model = Service
    template_name = "services/update.html"
    fields = ['name', 'type', 'abonent']