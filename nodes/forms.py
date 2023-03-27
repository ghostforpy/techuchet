from django.forms import ModelForm, IntegerField
from django.db.models import Q
from .models import Node

create_and_update_fileds = [
    'type', 
    'name', 
    'status', 
    # 'entity', 
    'building', 
    'ip_address',
    'parent'
]

class NodeUpdateForm(ModelForm):
    self_connectionunit = IntegerField(required=False)
    parent_node_connectionunit = IntegerField(required=False)

    class Meta:
        model = Node
        fields = create_and_update_fileds + [
            'self_connectionunit',
            'parent_node_connectionunit'
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        self_cons_qs = self.instance.connectionunit_set.filter(id=cleaned_data["self_connectionunit"])
        if cleaned_data.get("self_connectionunit"):
            if not self_cons_qs.exists():
                self.add_error('self_connectionunit', 'Порта с таким номером не существует.')
            else:
                parent = cleaned_data["parent"]
                if parent:
                    parent_cons_qs = parent.connectionunit_set.filter(id=cleaned_data["parent_node_connectionunit"])
                    if parent_cons_qs.exists():
                        # проверка, что порт принадлежит устройству
                        qs = parent_cons_qs.filter(Q(in_use_between_nodes=True) | Q(service__isnull=False))
                        if qs.exists():
                            # проверка, что порт свободен
                            conn = qs.get()
                            if hasattr(conn, 'children_node_connection_unit'):
                                if conn.children_node_connection_unit.node != self.instance:
                                    self.add_error('parent_node_connectionunit', 'Порт занят.')
                            else:
                                self.add_error('parent_node_connectionunit', 'Порт занят.')
                    else:
                        if cleaned_data.get("parent_node_connectionunit"):
                            self.add_error('parent_node_connectionunit', 'Порта с таким номером не существует.')
            if cleaned_data.get("parent_node_connectionunit") and not cleaned_data.get("parent_node_connectionunit"):
                # Выбран только свой порт
                self.add_error('parent_node_connectionunit', 'Порт не выбран.')
        if not cleaned_data.get("self_connectionunit") and cleaned_data.get("parent_node_connectionunit"):
            # Выбран только порт родительсокго устройства
            self.add_error('self_connectionunit', 'Порт не выбран.')
