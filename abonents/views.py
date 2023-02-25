# from django.shortcuts import render
# from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.db.models import Q

from .models import Abonent


create_and_update_fileds = [
    'name', 
    'type', 
    'phone', 
    'object_status', 
    'contract', 
]

class ListAndCreateAbonentView(CreateView):
    model = Abonent
    template_name = "abonents/list.html"
    fields = create_and_update_fileds
    success_url = '/abonents/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.model.objects.all()
        if self.request.GET.get('query'):
            query = self.request.GET.get('query')
            context["query"] = query
            qs = qs.filter(
                Q(name__name__icontains=query) |
                Q(type__name__icontains=query) |
                Q(object_status__name__icontains=query) |
                Q(ip_address__icontains=query) |
                Q(parent__name__name__icontains=query) |
                Q(building__type__name__icontains=query) |
                Q(building__street__icontains=query) |
                Q(building__region__name__icontains=query)
            )
        context["abonents"] = qs
        return context


class UpdateAbonentView(UpdateView):
    model = Abonent
    template_name = "abonents/update.html"
    fields = create_and_update_fileds
