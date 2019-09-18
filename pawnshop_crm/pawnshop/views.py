from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *

from .models import Client
from .forms import ClientForm


class CreditListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'credit/list.html')


class ClientCreateView(CreateView):
    template_name = 'client/create.html'
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('admin')
