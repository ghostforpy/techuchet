# from django.shortcuts import render
# from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.db.models import Q

from .models import Node


create_and_update_fileds = [
    'name', 
    'type', 
    'status', 
    # 'entity', 
    'building', 
    'ip_address',
    'parent'
]


class ListAndCreateNodeView(CreateView):
    model = Node
    template_name = "nodes/list.html"
    fields = create_and_update_fileds
    success_url = '/nodes/'

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
        context["nodes"] = qs
        return context


class UpdateNodeView(UpdateView):
    model = Node
    template_name = "nodes/update.html"
    fields = create_and_update_fileds