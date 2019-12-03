from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from ..models import ConfirmDocument, Client
from ..forms import ConfirmDocumentCreateForm


class ConfirmDocumentCreateView(CreateView):
    template_name = 'confirm_document/create.html'
    model = ConfirmDocument
    form_class = ConfirmDocumentCreateForm

    def get_context_data(self, **kwargs):
        client_pk = self.kwargs.get('client_pk')
        kwargs['client_pk'] = client_pk
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        client = get_object_or_404(Client, pk=self.kwargs.get('client_pk'))
        form.instance.client = client
        messages.add_message(self.request, messages.SUCCESS, 'Клиент успешно добавлен')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pawnshop:client_create') + f'?recent_client_pk={self.object.pk}'
