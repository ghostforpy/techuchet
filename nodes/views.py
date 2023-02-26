from datetime import datetime

from django.views.generic.edit import FormView, CreateView, UpdateView
from django.core.paginator import Paginator
from abonents.models import ObjectStatus
from buildings.models import Building, Region

from .models import Node, NodeName, NodeType


create_and_update_fileds = [
    'type', 
    'name', 
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

        if self.request.GET.get('type'):
            _type = self.request.GET.get('type')
            if _type.isdigit():
                qs = qs.filter(type__id=int(_type))
                context['select_type'] = int(_type)
        if self.request.GET.get('name'):
            name = self.request.GET.get('name')
            if name.isdigit():
                qs = qs.filter(name__id=int(name))
                context['select_name'] = int(name)
        if self.request.GET.get('building'):
            building = self.request.GET.get('building')
            if building.isdigit():
                qs = qs.filter(building__id=int(building))
                context['select_building'] = int(building)
        if self.request.GET.get('ip_address'):
            ip_address = self.request.GET.get('ip_address')
            qs = qs.filter(ip_address__icontains=ip_address)
            context['ip_address'] = ip_address
        if self.request.GET.get('object_status'):
            object_status = self.request.GET.get('object_status')
            if object_status.isdigit():
                qs = qs.filter(status__id=int(object_status))
                context['select_object_status'] = int(object_status)
        if self.request.GET.get('created_date'):
            created_date = self.request.GET.get('created_date')
            try:
                qs = qs.filter(
                    created_date=datetime.strptime(created_date, "%Y-%m-%d")
                )
                context['created_date'] = created_date
            except (ValueError, TypeError):
                pass
        if self.request.GET.get('change_date'):
            change_date = self.request.GET.get('change_date')
            try:
                qs = qs.filter(
                    change_date=datetime.strptime(change_date, "%Y-%m-%d")
                )
                context['change_date'] = change_date
            except (ValueError, TypeError):
                pass
        if self.request.GET.get('parent_node'):
            parent_node = self.request.GET.get('parent_node')
            if parent_node.isdigit():
                qs = qs.filter(parent__id=int(parent_node))
                context['parent_node'] = int(parent_node)
        if self.request.GET.get('region'):
            region = self.request.GET.get('region')
            if region.isdigit():
                qs = qs.filter(building__region__id=int(region))
                context['select_region'] = int(region)

        page = 1
        if self.request.GET.get('page'):
            page = self.request.GET.get('page')
            if page.isdigit():
                page = int(page)
        paginator = Paginator(qs, 20)
        context['nodes_pages'] = paginator.num_pages
        context["nodes"] = paginator.get_page(page)

        context["object_statuses"] = ObjectStatus.objects.all()
        context['buildings'] = Building.objects.select_related('region').all()
        context['node_names'] = NodeName.objects.select_related('type').all()
        context["node_types"] = NodeType.objects.all()
        context["parent_nodes"] = Node.objects.all()
        context["regions"] = Region.objects.all()
        return context


class UpdateNodeView(UpdateView):
    model = Node
    template_name = "nodes/update.html"
    fields = create_and_update_fileds
    success_url = '/nodes/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['node_names'] = NodeName.objects.select_related('type').all()
        context["regions"] = Region.objects.all()
        context['buildings'] = Building.objects.select_related('region').all()
        return context