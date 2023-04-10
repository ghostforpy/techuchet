from datetime import datetime, timedelta
from django.utils import timezone

from excel_response import ExcelResponse

from abonents.models import Abonent, ObjectStatus
from nodes.models import Node


def abonents_report(request):
    now = timezone.now()
    delta = timedelta(days=-31)
    status = ObjectStatus.objects.get(name="Готов")
    qs = Abonent.objects.select_related('type').filter(
        object_status=status,
        enable_date__gte=now+delta
    )
    data = [
        ['Номер договора', 'Имя', 'Тип абонента', 'Телефон', 'Дата подключения']
    ]
    for abonent in qs:
        data.append(
            [abonent.contract, abonent.name, abonent.type.name, abonent.phone, abonent.enable_date]
        )
    data.append(["" for _ in range(5)])
    l = ["" for _ in range(5)]
    l[0] = "Наименование отчёта:"
    l[1] = '"Абоненты для подключения"'
    data.append([i for i in l])
    l[0] = "Дата составления отчёта:"
    l[1] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    data.append(l)
    return ExcelResponse(data, 'abonents')


def abonents_repair_report(request):
    status = ObjectStatus.objects.get(name="Ремонт")
    qs = Abonent.objects.select_related('type').filter(
        object_status=status
    )
    data = [
        ['Номер договора', 'Имя', 'Тип абонента', 'Телефон', 'Дата подключения']
    ]
    for abonent in qs:
        data.append(
            [abonent.contract, abonent.name, abonent.type.name, abonent.phone, abonent.enable_date]
        )
    data.append(["" for _ in range(5)])
    l = ["" for _ in range(5)]
    l[0] = "Наименование отчёта:"
    l[1] = '"Ремонты абоненты"'
    data.append([i for i in l])
    l[0] = "Дата составления отчёта:"
    l[1] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    data.append(l)
    return ExcelResponse(data, 'abonents_repair')


def repair_works_report(request):
    status = ObjectStatus.objects.get(name="Ремонт")
    nodes = Node.objects.filter(status=status).select_related("type", "name", "building")
    def abonent_nums(node):
        n = node.connectionunit_set.filter(service__abonent__isnull=False).count()
        if node.node_set.count() > 0:
            for _node in node.node_set.all():
                n += abonent_nums(_node)
        return n
    data = [
        ['Наименование', 'Тип', 'Здание', 'IP адрес', 'Количество абонентов']
    ]
    for node in nodes:
        try:
            abonents = abonent_nums(node)
        except RecursionError:
            abonents = "Подключение оборудования зациклено"
        data.append(
            [
                node.name.name, 
                node.type.name, 
                f'{node.building.region.name}, {str(node.building)}',
                node.ip_address,
                abonents
            ]
        )
    data.append(["" for _ in range(5)])
    l = ["" for _ in range(5)]
    l[0] = "Наименование отчёта:"
    l[1] = '"Ремонтные работы"'
    data.append([i for i in l])
    l[0] = "Дата составления отчёта:"
    l[1] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    data.append(l)
    return ExcelResponse(data, 'repair_nodes')