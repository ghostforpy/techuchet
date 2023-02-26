# from django.shortcuts import render
# from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView

from django.db.models import Q
from django.http import JsonResponse

from abonents.models import Abonent

from .models import Service, ServiceName



# class ServiceListView(ListView):
#     model = Service
#     template_name = "services/list.html"
#     context_object_name = 'services'
create_and_update_fileds = [
    'type', 
    'name', 
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
        context['service_names'] = ServiceName.objects.select_related('type').all()
        context["abonent_names"] = Abonent.objects.all()
        context["services"] = qs
        return context


class UpdateServiceView(UpdateView):
    model = Service
    template_name = "services/update.html"
    fields = create_and_update_fileds
    success_url = '/services/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_names'] = ServiceName.objects.select_related('type').all()
        context["abonent_names"] = Abonent.objects.all()
        return context


class ServiceNameListView(ListView):

    model = ServiceName
    context_object_name = 'service_names'

    def get_queryset(self):
        return super().get_queryset().filter(type__id=self.kwargs['type_pk'])
    
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse({
            'service_names': [i for i in context['service_names'].values('name', 'id')]
        })