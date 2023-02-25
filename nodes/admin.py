from django.contrib import admin


from .models import Node, NodeType, NodeName


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    pass

@admin.register(NodeType)
class NodeTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(NodeName)
class NodeNameAdmin(admin.ModelAdmin):
    pass