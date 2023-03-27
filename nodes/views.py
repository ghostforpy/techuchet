from datetime import datetime

from django.views.generic.edit import FormView, CreateView, UpdateView
from django.core.paginator import Paginator
from django.db.models import F
from abonents.models import ObjectStatus
from connections.models import ConnectionUnit, ConnectionUnitType
from buildings.models import Building, Region

from .models import Node, NodeName, NodeType
from .forms import NodeUpdateForm, create_and_update_fileds


class ListAndCreateNodeView(CreateView):
    model = Node
    template_name = "nodes/list.html"
    fields = create_and_update_fileds
    # success_url = '/nodes/'

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
        if self.request.GET.get('name'):
            name = self.request.GET.get('name')
            if name.isdigit():
                qs = qs.filter(name__id=int(name))
                filtered = True
                context['select_name'] = int(name)
        if self.request.GET.get('building'):
            building = self.request.GET.get('building')
            if building.isdigit():
                qs = qs.filter(building__id=int(building))
                filtered = True
                context['select_building'] = int(building)
        if self.request.GET.get('ip_address'):
            ip_address = self.request.GET.get('ip_address')
            qs = qs.filter(ip_address__icontains=ip_address)
            filtered = True
            context['ip_address'] = ip_address
        if self.request.GET.get('parent_ip_address'):
            parent_ip_address = self.request.GET.get('parent_ip_address')
            qs = qs.filter(parent__ip_address__icontains=parent_ip_address)
            filtered = True
            context['parent_ip_address'] = parent_ip_address
        if self.request.GET.get('object_status'):
            object_status = self.request.GET.get('object_status')
            if object_status.isdigit():
                qs = qs.filter(status__id=int(object_status))
                context['select_object_status'] = int(object_status)
                filtered = True
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
        # if self.request.GET.get('parent_node'):
        #     parent_node = self.request.GET.get('parent_node')
        #     if parent_node.isdigit():
        #         qs = qs.filter(parent__id=int(parent_node))
        #         filtered = True
        #         context['parent_node'] = int(parent_node)
        if self.request.GET.get('region'):
            region = self.request.GET.get('region')
            if region.isdigit():
                qs = qs.filter(building__region__id=int(region))
                filtered = True
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
        context['all_nodes'] = Node.objects.all() # поправить
        context["node_types"] = NodeType.objects.all()
        # context["parent_nodes"] = Node.objects.all() # для select parent_node
        context["regions"] = Region.objects.all()
        context["filtered"] = filtered
        return context


class UpdateNodeView(UpdateView):
    model = Node
    template_name = "nodes/update.html"
    success_url = '/nodes/'
    form_class = NodeUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['node_names'] = NodeName.objects.select_related('type').all()
        context["regions"] = Region.objects.all()
        context['buildings'] = Building.objects.select_related('region').all()
        context['all_nodes'] = Node.objects.all()
        context['connection_unit_types'] = ConnectionUnitType.objects.all()
        context["connection_units"] = ConnectionUnit.objects.filter(
            service__isnull=True,
        ).values("id", "number").annotate(
            node_id=F("node__pk"), 
            node_ip=F("node__ip_address"),
            connection_name=F("type__name"),
            parent_connection=F("parent_node_connection_unit__pk"),
            connect_to_children=F("children_node_connection_unit__node__id")
        )
        return context
    
    def form_valid(self, form):
        self_connectionunit_id = form.cleaned_data.get("self_connectionunit")
        parent_node_connectionunit_id = form.cleaned_data.get("parent_node_connectionunit")

        response = super().form_valid(form)
        if self_connectionunit_id and parent_node_connectionunit_id:
            old_self_conn = ConnectionUnit.objects.filter(
                node=form.instance,
                parent_node_connection_unit__isnull=False,
                in_use_between_nodes=True
            )
            def set_connection():
                connectionunit = form.instance.connectionunit_set.filter(id=self_connectionunit_id).get()
                parent_node_connectionunit = form.instance.parent.connectionunit_set.filter(
                    id=parent_node_connectionunit_id
                ).get()
                connectionunit.parent_node_connection_unit = parent_node_connectionunit
                connectionunit.save()

            if old_self_conn.exists():
                # до этого уже было соединение
                old_self_conn = old_self_conn.get()
                if old_self_conn.id != self_connectionunit_id:
                    # сброс старого соединения
                    old_self_conn.parent_node_connection_unit = None
                    old_self_conn.save()
                    # установка нового соединения
                    ConnectionUnit.objects.filter(
                        id=self_connectionunit_id
                    ).update(
                        parent_node_connection_unit=parent_node_connectionunit_id,
                        in_use_between_nodes=True
                    )
                    # обновление статуса встречного порта
                    ConnectionUnit.objects.filter(
                        id=parent_node_connectionunit_id
                    ).update(in_use_between_nodes=True)
                else:
                    # свой порт не менялся
                    if old_self_conn.parent_node_connection_unit.id != parent_node_connectionunit_id:
                        # встречный порт поменялся
                        set_connection()
            else:
                # новое соединение
                set_connection()
        return response