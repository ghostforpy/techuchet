from datetime import datetime

from django.views.generic.edit import FormView, CreateView, UpdateView
from django.core.paginator import Paginator
from buildings.models import Building, Region

from .models import Abonent, ObjectStatus, AbonentType


create_and_update_fileds = [
    'name', 
    'type', 
    'phone', 
    'building',
    'object_status', 
    'contract', 
]

class ListAndCreateAbonentView(CreateView):
    model = Abonent
    template_name = "abonents/list.html"
    fields = create_and_update_fileds
    # success_url = '/abonents/'

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.model.objects.all()
        filtered = False
        if self.request.GET.get('contract'):
            contract = self.request.GET.get('contract')
            qs = qs.filter(contract__icontains=contract)
            filtered = True
            context['contract'] = contract
        if self.request.GET.get('name'):
            name = self.request.GET.get('name')
            qs = qs.filter(name__icontains=name)
            filtered = True
            context['name'] = name
        if self.request.GET.get('phone'):
            phone = self.request.GET.get('phone')
            qs = qs.filter(phone__icontains=phone)
            filtered = True
            context['phone'] = phone
        if self.request.GET.get('type'):
            _type = self.request.GET.get('type')
            if _type.isdigit():
                qs = qs.filter(type__id=int(_type))
                filtered = True
                context['select_type'] = int(_type)
        if self.request.GET.get('object_status'):
            object_status = self.request.GET.get('object_status')
            if object_status.isdigit():
                qs = qs.filter(object_status__id=int(object_status))
                filtered = True
                context['select_object_status'] = int(object_status)
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
        if self.request.GET.get('disable_date'):
            disable_date = self.request.GET.get('disable_date')
            try:
                qs = qs.filter(
                    disable_date=datetime.strptime(disable_date, "%Y-%m-%d")
                )
                filtered = True
                context['disable_date'] = disable_date
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
        page = 1
        if self.request.GET.get('page'):
            page = self.request.GET.get('page')
            if page.isdigit():
                page = int(page)
        paginator = Paginator(qs, 20)
        context['abonents_pages'] = paginator.num_pages
        context["abonents"] = paginator.get_page(page)
        context["object_statuses"] = ObjectStatus.objects.all()
        context["abonent_types"] = AbonentType.objects.all()
        context['buildings'] = Building.objects.select_related('region').all()
        context["regions"] = Region.objects.all()
        context["filtered"] = filtered
        return context


class UpdateAbonentView(UpdateView):
    model = Abonent
    template_name = "abonents/update.html"
    fields = [i for i in create_and_update_fileds if i != 'building'] + ['disable_date']
    success_url = '/abonents/'
