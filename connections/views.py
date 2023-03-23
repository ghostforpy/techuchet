# from django.shortcuts import render
# from django.views.generic import ListView
import json

from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from abonents.models import ObjectStatus
from nodes.models import Node

from services.models import Service

from .models import ConnectionUnit, ConnectionUnitType


create_and_update_fileds = [
    'type', 
    'number',
    'node',
    'rate',
    'status', 
    'service', 
]


class ListAndCreateConnectionUnitView(CreateView):
    model = ConnectionUnit
    template_name = "connections/list.html"
    fields = create_and_update_fileds
    # success_url = '/connections/'

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.model.objects.all()
        filtered = False
        if self.request.GET.get('type'):
            _type = self.request.GET.get('type')
            if _type.isdigit():
                qs = qs.filter(type__id=int(_type))
                filtered = True
                context['select_type'] = int(_type)
        if self.request.GET.get('service'):
            service = self.request.GET.get('service')
            qs = qs.filter(
                Q(service__name__name__icontains=service) |
                Q(service__type__name__icontains=service) |
                Q(service__abonent__name__icontains=service) |
                Q(service__abonent__contract__icontains=service)
            )
            filtered = True
            context['service'] = int(service)
        if self.request.GET.get('ip_address'):
            ip_address = self.request.GET.get('ip_address')
            qs = qs.filter(
                node__ip_address__icontains=ip_address
            )
            filtered = True
            context['ip_address'] = ip_address
        if self.request.GET.get('object_status'):
            object_status = self.request.GET.get('object_status')
            if object_status.isdigit():
                qs = qs.filter(status__id=int(object_status))
                filtered = True
                context['select_object_status'] = int(object_status)
        # if self.request.GET.get('node'):
        #     node = self.request.GET.get('node')
        #     if node.isdigit():
        #         qs = qs.filter(node__id=int(node))
        #         context['select_node'] = int(node)
        if self.request.GET.get('number'):
            number = self.request.GET.get('number')
            if number.isdigit():
                qs = qs.filter(number=int(number))
                filtered = True
                context['number'] = int(number)
        if self.request.GET.get('rate'):
            rate = self.request.GET.get('rate')
            if rate.isdigit():
                qs = qs.filter(rate=int(rate))
                filtered = True
                context['rate'] = int(rate)
        page = 1
        if self.request.GET.get('page'):
            page = self.request.GET.get('page')
            if page.isdigit():
                page = int(page)
        paginator = Paginator(qs, 20)
        context['connections_pages'] = paginator.num_pages
        context["service_names"] = Service.objects.select_related('abonent').all()
        context["connections"] = paginator.get_page(page)
        context["connection_types"] = ConnectionUnitType.objects.all()
        context["services"] = Service.objects.all()
        context["object_statuses"] = ObjectStatus.objects.all()
        context["filtered"] = filtered
        context["nodes"] = Node.objects.all()
        return context


class UpdateConnectionUnitView(UpdateView):
    model = ConnectionUnit
    template_name = "connections/update.html"
    fields = create_and_update_fileds
    success_url = '/connections/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_names"] = Service.objects.select_related('abonent').all()
        context["nodes"] = Node.objects.all()
        return context


@csrf_exempt
def create_connection_units(request):
    data = json.loads(request.body)
    node_id = data["node_id"]
    node = get_object_or_404(Node, id=node_id)
    connections = []
    number = 1
    for connection_unit in data["connection_units"]:
        connection_type = get_object_or_404(ConnectionUnitType, id=connection_unit["type_id"])
        for _ in range(connection_unit["nums"]):
            connections.append(
                ConnectionUnit(type=connection_type, node=node, number=number)
            )
            number += 1
    ConnectionUnit.objects.bulk_create(connections)
    return JsonResponse({"status": "ok"})
