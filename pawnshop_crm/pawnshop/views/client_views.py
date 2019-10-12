from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import *

from accounts.mixins import GroupRequiredMixin
from ..models import *
from ..forms import *


class ClientCreateView(GroupRequiredMixin, CreateView):
    group_required = [u'Cashier', u'Admin']
    template_name = 'client/create.html'
    model = Client
    form_class = ClientCreateForm

    def get_context_data(self, **kwargs):
        try:
            recent_client_pk = self.request.GET.get('recent_client_pk')
            recent_client = Client.objects.get(pk=recent_client_pk)
            kwargs['recent_client'] = recent_client
            return super().get_context_data(**kwargs)
        except Client.DoesNotExist:
            return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('pawnshop:confirm_document_create', kwargs={'client_pk': self.object.pk})


class ClientChooseView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        client_pk = self.request.GET.get('client_pk')
        return reverse('pawnshop:loan_create', kwargs={
            'client_pk': client_pk
        })


class ClientDetailAjaxView(View):
    def get(self, request, *args, **kwargs):
        client_pk = int(self.request.GET.get('client_pk'))
        client = get_object_or_404(Client, pk=client_pk)
        data = {
            'client': {
                'first_name': client.first_name,
                'last_name': client.last_name,
                'middle_name': client.middle_name,
                'birth_date': client.birth_date,
                'iin': client.confirm_document.iin
            }
        }
        return JsonResponse(data)


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
