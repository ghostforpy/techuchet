# from django.shortcuts import render
# from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.db.models import Q

from .models import Service



# class ServiceListView(ListView):
#     model = Service
#     template_name = "services/list.html"
#     context_object_name = 'services'
create_and_update_fileds = [
    'name', 
    'type', 
    'abonent', 
    'status', 
]


class ListAndCreateServiceView(CreateView):
    model = Service
    template_name = "services/list.html"
    fields = create_and_update_fileds
    success_url = '/services/'


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
                Q(abonent__name__icontains=query) |
                Q(abonent__phone__icontains=query) |
                Q(abonent__contract__icontains=query)
            )
        context["services"] = qs
        return context


class UpdateServiceView(UpdateView):
    model = Service
    template_name = "services/update.html"
    fields = create_and_update_fileds