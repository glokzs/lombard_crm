from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import *

from .models import Client, ConfirmDocument
from .forms import ClientForm, ConfirmDocumentForm


class CreditListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'credit/list.html')


class ClientCreateView(CreateView):
    template_name = 'client/create.html'
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('pawnshop:confirm_document_create') + f'?client_pk={self.object.pk}'


class ConfirmDocumentCreateView(CreateView):
    template_name = 'confirm_document/create.html'
    model = ConfirmDocument
    form_class = ConfirmDocumentForm

    def get_context_data(self, **kwargs):
        kwargs['client_pk'] = self.request.GET.get('client_pk')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        client = get_object_or_404(Client, pk=self.request.POST.get('client_pk'))
        form.instance.client = client
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pawnshop:client_create')
