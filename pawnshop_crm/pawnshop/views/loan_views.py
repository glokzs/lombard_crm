from datetime import datetime, timedelta

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import *

from ..models import *
from ..forms import *


class LoanCalculateAjaxView(View):
    def get(self, request, *args, **kwargs):
        client_amount = float(self.request.GET.get('client_amount'))
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
        interest_rate = float(self.request.session.get('pledge_item_list')[0]['interest_rate'])
        print(interest_rate)
        total_amount = int(100 * client_amount / (99 - interest_rate * duration))
        return total_amount


# class LoanCreateView(CreateView):
#     model = Loan
#     template_name = 'loan/create.html'
#     form_class = LoanCreateForm
#
#     def get_context_data(self, **kwargs):
#         kwargs['client_pk'] = self.kwargs.get('client_pk')
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         data = form.cleaned_data
#         pledge_item = get_object_or_404(PledgeItem, pk=self.kwargs.get('pledge_item_pk'))
#         form.instance.date_of_expire = self._get_date_of_expire(data.get('duration'))
#         form.instance.client = get_object_or_404(Client, pk=self.kwargs.get('client_pk'))
#         form.instance.pledge_item = pledge_item
#         interest_rate = pledge_item.category.interest_rate
#         client_amount = int(self.request.POST.get('client_amount'))
#         duration = int(self.request.POST.get('duration'))
#
#         form.instance.total_amount = self._calculate_total_amount(client_amount, duration, interest_rate)
#         return super().form_valid(form)
#
#     def _calculate_total_amount(self, client_amount, duration, interest_rate):
#         total_amount = int(100 * client_amount / (99 - interest_rate * duration))
#         return total_amount
#
#     def _get_date_of_expire(self, duration):
#         return datetime.now() + timedelta(days=duration)
#
#     def get_success_url(self):
#         return reverse('pawnshop:loan_list')

class LoanCreateView(CreateView):
    model = Loan
    template_name = 'loan/create.html'
    form_class = LoanCreateForm

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.filter(subcategories__isnull=False).distinct()
        kwargs['client_pk'] = self.kwargs.get('client_pk')
        kwargs['total_price'] = self._get_total_evaluation_price()
        return super().get_context_data(**kwargs)

    def _get_total_evaluation_price(self):
        total_price = 0
        if not self.request.session.get('pledge_item_list'):
            return total_price

        for pledge_item in self.request.session.get('pledge_item_list'):
            total_price += int(pledge_item.get('price'))
        return total_price

    def form_valid(self, form):
        pass

    def get_success_url(self):
        return reverse('pawnshop:loan_list')


class LoanListView(ListView):
    template_name = 'loan/list.html'
    context_object_name = 'loans'
    model = Loan
