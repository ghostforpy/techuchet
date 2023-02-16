# from django.shortcuts import render
# from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView

from .models import Node



# class NodeListView(ListView):
#     model = Node
#     template_name = "nodes/list.html"
#     context_object_name = 'nodes'

class ListAndCreateNodeView(CreateView):
    model = Node
    template_name = "nodes/list.html"
    fields = ['name', 'type', 'status', 'entity', 'buiilding', 'ip_address']
    success_url = '/nodes/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nodes"] = self.model.objects.all()
        return context

class UpdateNodeView(UpdateView):
    model = Node
    template_name = "nodes/update.html"
    fields = ['name', 'type', 'status', 'entity', 'buiilding', 'ip_address']