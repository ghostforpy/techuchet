# from django.shortcuts import render
# from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.db.models import Q

from .models import ConnectionUnit


create_and_update_fileds = [
    'type', 
    'number',
    'node',
    'status', 
    'service', 
]


class ListAndCreateConnectionUnitView(CreateView):
    model = ConnectionUnit
    template_name = "connections/list.html"
    fields = create_and_update_fileds
    success_url = '/connections/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.model.objects.all()
        if self.request.GET.get('query'):
            query = self.request.GET.get('query')
            context["query"] = query
            qs = qs.filter(
                Q(name__name__icontains=query) |
                Q(type__name__icontains=query) |
                Q(entity__name__icontains=query) |
                Q(status__name__icontains=query) |
                Q(ip_address__icontains=query) |
                Q(parent__name__name__icontains=query) |
                Q(building__type__name__icontains=query) |
                Q(building__street__icontains=query) |
                Q(building__region__name__icontains=query)
            )
        context["connections"] = qs
        return context


class UpdateConnectionUnitView(UpdateView):
    model = ConnectionUnit
    template_name = "connections/update.html"
    fields = create_and_update_fileds