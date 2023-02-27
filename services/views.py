from datetime import datetime

from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse

from abonents.models import Abonent, ObjectStatus

from .models import Service, ServiceName, ServiceType



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
        filtered = False
        if self.request.GET.get('created_date'):
            created_date = self.request.GET.get('created_date')
            try:
                qs = qs.filter(
                    created_date=datetime.strptime(created_date, "%Y-%m-%d")
                )
                filtered = True
                context['created_date'] = created_date
            except (ValueError, TypeError):
                pass
        if self.request.GET.get('change_date'):
            change_date = self.request.GET.get('change_date')
            try:
                qs = qs.filter(
                    change_date=datetime.strptime(change_date, "%Y-%m-%d")
                )
                filtered = True
                context['change_date'] = change_date
            except (ValueError, TypeError):
                pass
        if self.request.GET.get('object_status'):
            object_status = self.request.GET.get('object_status')
            if object_status.isdigit():
                qs = qs.filter(status__id=int(object_status))
                filtered = True
                context['select_object_status'] = int(object_status)
        if self.request.GET.get('service_name'):
            service_name = self.request.GET.get('service_name')
            if service_name.isdigit():
                qs = qs.filter(name__id=int(service_name))
                filtered = True
                context['select_service_name'] = int(service_name)
        if self.request.GET.get('type'):
            _type = self.request.GET.get('type')
            if _type.isdigit():
                qs = qs.filter(type__id=int(_type))
                filtered = True
                context['select_type'] = int(_type)
        # if self.request.GET.get('abonent'):
        #     abonent = self.request.GET.get('abonent')
        #     if abonent.isdigit():
        #         qs = qs.filter(abonent__id=int(abonent))
        #         filtered = True
        #         context['select_abonent'] = int(abonent)
        if self.request.GET.get('contract'):
            contract = self.request.GET.get('contract')
            
            qs = qs.filter(abonent__contract__icontains=contract)
            filtered = True
            context['contract'] = contract

        page = 1
        if self.request.GET.get('page'):
            page = self.request.GET.get('page')
            if page.isdigit():
                page = int(page)
        paginator = Paginator(qs, 20)
        context['services_pages'] = paginator.num_pages
        context["services"] = paginator.get_page(page)
        context["filtered"] = filtered
        context['service_names'] = ServiceName.objects.select_related('type').all()
        context['service_types'] = ServiceType.objects.all()
        context["abonent_names"] = Abonent.objects.all()
        context["object_statuses"] = ObjectStatus.objects.all()
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