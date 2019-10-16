from datetime import datetime, timedelta

from django.db.models import Q
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
        kwargs['total_price'] = self._get_total_price()
        return super().get_context_data(**kwargs)

    def _get_total_price(self):
        total_price = 0
        if not self.request.session.get('pledge_item_list'):
            return total_price
        for pledge_item in self.request.session.get('pledge_item_list'):
            total_price += int(pledge_item.get('price'))
        return total_price

    def form_valid(self, form):
        form.instance.date_of_expire = self._get_expire_date(form.cleaned_data.get('duration'))
        form.instance.total_amount = form.cleaned_data.get('total_amount')
        form.instance.client = get_object_or_404(Client, pk=self.kwargs.get('client_pk'))
        return super().form_valid(form)

    def _get_expire_date(self, duration):
        return datetime.now() + timedelta(duration)

    def get_success_url(self):
        for item in self.request.session.get('pledge_item_list'):
            pledge_item = get_object_or_404(PledgeItem, pk=int(item.get('pk')))
            pledge_item.loan = self.object
            pledge_item.save()
        self.request.session.clear()
        return reverse('pawnshop:loan_detail')


class LoanListView(ListView):
    template_name = 'loan/list.html'
    context_object_name = 'loans'
    model = Loan


class LoantListAjaxView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        first_name_query = Q(first_name__icontains=query)
        last_name_query = Q(last_name__icontains=query)
        iin_query = Q(confirm_document__iin__icontains=query)
        ticket_number_query = Q(id__icontains=query)
        loans = Loan.objects.filter(first_name_query | last_name_query | iin_query | ticket_number_query)

        data = {
            'loans': []
        }
        if not query:
            return JsonResponse(data)

        for loan in loans:
            loan_object = {
                'pk': loan.id,
                'first_name': loan.client.first_name,
                'last_name': loan.client.last_name,
                'category': loan.pledge_item.category.name,
                'created_at': loan.created_at,
                'duration': loan.duration,
                'date_of_expire': loan.date_of_expire,
                'total_amount': loan.total_amount,
                'interest_rate': loan.pledge_item.category.interest_rate
            }
            data['loans'].append(loan_object)
        return JsonResponse(data)

class LoanDetailView(DetailView):
    template_name = 'loan/detail.html'
    context_object_name = 'loan'
    model = Loan
    pk_url_kwarg = 'loan_pk'