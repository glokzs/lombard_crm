from datetime import datetime, timedelta

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import *

from ..models import *
from ..forms import *


class LoanCalculateAjaxView(View):
    def get(self, request, *args, **kwargs):
        client_amount = int(self.request.GET.get('client_amount'))
        duration = int(self.request.GET.get('duration'))

        data = {
            'duration_error': False,
            'client_amount_error': False
        }

        # check duration
        if duration < 5 or duration > 30:
            data['duration_error'] = True

        # check client_amount
        MINIMUM_CLIENT_AMOUNT = 1000
        if client_amount < MINIMUM_CLIENT_AMOUNT:
            data['client_amount_error'] = True

        data['total_amount'] = self._calculate_total_amount(client_amount, duration)
        return JsonResponse(data=data)

    def _calculate_total_amount(self, client_amount, duration):
        pledge_item_pk = self.request.session.get('pledge_item_pk')
        interest_rate = get_object_or_404(PledgeItem, pk=pledge_item_pk).category.interest_rate
        total_amount = 100 * client_amount / (99 - interest_rate * duration)
        return total_amount


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

