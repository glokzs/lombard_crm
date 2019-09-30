from datetime import datetime, timedelta

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import *

from ..models import *
from ..forms import *


class LoanCalculateAjaxView(View):
    def get(self, request, *args, **kwargs):
        requested_amount = int(self.request.GET.get('requested_amount'))
        duration = int(self.request.GET.get('duration'))
        interest_rate = 0.9
        total_amount = round(requested_amount * 100 / (99 - (duration * interest_rate)))

        return JsonResponse({"total_amount": total_amount})


class LoanCreateView(CreateView):
    model = Loan
    template_name = 'loan/create.html'
    form_class = LoanCreateForm

    def form_valid(self, form):
        duration = int(self.request.POST.get('duration'))
        form.instance.date_of_expire = self._get_date_of_expire(duration)
        form.instance.client = get_object_or_404(Client, pk=self.request.session.get('client_pk'))
        form.instance.pledge_item = get_object_or_404(PledgeItem, pk=self.request.session.get('pledge_item_pk'))
        return super().form_valid(form)

    def _get_date_of_expire(self, duration):
        return datetime.now() + timedelta(days=duration)

    def get_success_url(self):
        self.request.session.pop('client_pk', None)
        self.request.session.pop('pledge_item_pk', None)
        return reverse('pawnshop:credit_list')

