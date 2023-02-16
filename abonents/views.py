# from django.shortcuts import render
# from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from .models import Abonent
# from .forms import AbonentForm


# class AbonentListView(ListView):
#     model = Abonent
#     template_name = "abonents/list.html"
#     context_object_name = 'abonents'


# class AbonentCreateView(FormView):
#     template_name = 'abonents/list.html'
#     form_class = AbonentForm
#     success_url = '/abonents/'


# class AbonentCreateView(CreateView):
#     model = Abonent
#     fields = ['created_date']
#     template_name = "abonents/list.html"

class ListAndCreateAbonentView(CreateView):
    model = Abonent
    template_name = "abonents/list.html"
    fields = ['name' ,'type', 'object_status']
    success_url = '/abonents/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["abonents"] = self.model.objects.all()
        return context


class UpdateAbonentView(UpdateView):
    model = Abonent
    template_name = "abonents/update.html"
    fields = ['name' ,'type', 'object_status']
