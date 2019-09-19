from django.db.models import Q
from django.http import JsonResponse
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

    def get_context_data(self, **kwargs):
        recent_client_pk = self.request.GET.get('recent_client_pk')
        if recent_client_pk:
            recent_client = get_object_or_404(Client, pk=self.request.GET.get('recent_client_pk'))
            kwargs['recent_client'] = recent_client
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('pawnshop:confirm_document_create', kwargs={'client_pk': self.object.pk})


class ClientListAjaxView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        first_name_query = Q(first_name__icontains=query)
        last_name_query = Q(last_name__icontains=query)
        iin_query = Q(confirm_document__iin__icontains=query)
        clients = Client.objects.filter(first_name_query | last_name_query | iin_query)

        data = {
            'clients': []
        }
        if not query:
            return JsonResponse(data)

        for client in clients:
            client_object = {
                'pk': client.pk,
                'first_name': client.first_name,
                'last_name': client.last_name,
                'middle_name': client.middle_name,
                'birth_date': client.birth_date,
                'iin': client.confirm_document.iin
            }
            data['clients'].append(client_object)
        return JsonResponse(data)


class ConfirmDocumentCreateView(CreateView):
    template_name = 'confirm_document/create.html'
    model = ConfirmDocument
    form_class = ConfirmDocumentForm

    def get_context_data(self, **kwargs):
        kwargs['client_pk'] = self.kwargs.get('client_pk')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        client = get_object_or_404(Client, pk=self.kwargs.get('client_pk'))
        form.instance.client = client
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pawnshop:client_create') + f"?recent_client_pk={self.kwargs.get('client_pk')}"
