from datetime import timedelta
from django.utils import timezone

from excel_response import ExcelResponse

from abonents.models import Abonent, ObjectStatus


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
    return ExcelResponse(data, 'abonents')