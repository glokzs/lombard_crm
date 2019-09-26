from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import *

from ..models import *
from ..forms import *


class ConfirmDocumentCreateView(CreateView):
    template_name = 'confirm_document/create.html'
    model = ConfirmDocument
    form_class = ConfirmDocumentForm

    def get_context_data(self, **kwargs):
        kwargs['client_pk'] = self.kwargs.get('client_pk')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        client = get_object_or_404(Client, pk=self.request.session['client_pk'])
        form.instance.client = client
        return super().form_valid(form)

    def get_success_url(self):
        self.request.session['recent_client_pk'] = self.object.pk
        return reverse('pawnshop:client_create', )
