import json
import os
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import *
from django.contrib import messages

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
        total_amount = int(100 * client_amount / (99 - interest_rate * duration))
        return total_amount


class LoanCreateView(UserPassesTestMixin, CreateView):
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
        form.instance.status = Loan.STATUS_OPEN
        form.save()
        self.record_operation(form.instance)
        messages.add_message(self.request, messages.SUCCESS, 'Залог успешно добавлен')
        return super().form_valid(form)

    def _get_expire_date(self, duration):
        return datetime.now() + timedelta(duration)

    def get_success_url(self):
        pledge_item_list = self.request.session.get('pledge_item_list')
        if pledge_item_list:
            for item in pledge_item_list:
                pledge_item = get_object_or_404(PledgeItem, pk=int(item.get('pk')))
                pledge_item.loan = self.object
                pledge_item.save()
        self.request.session.pop('pledge_item_list', None)
        return reverse('pawnshop:loan_detail', kwargs={'loan_pk': self.object.pk})

    def test_func(self):
        return self.request.user.has_perm('accounts.add_loan')

    def record_operation(self, loan):
        Operation.objects.create(
            employee=self.request.user,
            amount=-1 * loan.client_amount,
            loan=loan,
            operation_type=Operation.TYPE_LOAN_CREATE
        )


class LoanListView(UserPassesTestMixin, ListView):
    template_name = 'loan/list.html'
    context_object_name = 'loans'
    model = Loan
    ordering = ['-created_at']

    def test_func(self):
        return self.request.user.has_perm('accounts.add_loan')

    def get_context_data(self, **kwargs):
        Loan.expire_loans()
        return super().get_context_data(**kwargs)


class LoanListAjaxView(View):
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


class LoanDetailView(UserPassesTestMixin, DetailView):
    template_name = 'loan/detail.html'
    context_object_name = 'loan'
    model = Loan
    pk_url_kwarg = 'loan_pk'

    def get_context_data(self, **kwargs):
        # self._generate_ticket()
        loan = get_object_or_404(Loan, pk=self.kwargs.get('loan_pk'))

        kwargs['total_price'] = self._get_total_price()
        kwargs['interest_rate'] = self._get_interest_rate()
        # kwargs['ticket_url'] = os.path.join(settings.MEDIA_URL, loan.ticket.file_path)
        kwargs['is_closed'] = True if loan.status == Loan.STATUS_CLOSED else False
        kwargs['amount_to_buyout'] = self.get_amount_to_buyout()
        kwargs['expired_days'] = self.object.get_expired_days()

        Loan.expire_loans()
        return super().get_context_data(**kwargs)

    # def _generate_ticket(self):
    #     file_name = f'Залоговый_билет_{self.kwargs.get("loan_pk")}'
    #     loan = get_object_or_404(Loan, pk=self.kwargs.get('loan_pk'))
    #
    #     context = {
    #         'loan': get_object_or_404(Loan, pk=self.kwargs.get('loan_pk'))
    #     }
    #     rendered_ticket = render(self.request, 'ticket/ticket.html', context=context)
    #
    #     output_file_name = os.path.join(settings.TICKET_FOLDER_PATH, file_name)
    #     pdfkit.from_string(rendered_ticket.content.decode(), f'{output_file_name}.pdf')

    def _get_interest_rate(self):
        return self.object.pledge_items.first().category.interest_rate

    def _get_total_price(self):
        total_price = 0
        for pledge_item in self.object.pledge_items.all():
            total_price += pledge_item.price
        return total_price

    def get_amount_to_buyout(self):
        fine = 2.5  # Штраф в день
        expired_days = self.object.get_expired_days()
        if expired_days:
            return float(self.object.total_amount) * fine * expired_days / 100

    def test_func(self):
        return self.request.user.has_perm('accounts.add_loan')


class LoanBuyoutView(UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        loan_pk = self.kwargs.get('loan_pk')
        loan = get_object_or_404(Loan, pk=loan_pk)
        loan.status = Loan.STATUS_CLOSED
        loan.save()
        self.record_operation(loan)

        messages.add_message(self.request, messages.SUCCESS, 'Залог успешно выкуплен')
        return redirect(reverse('pawnshop:loan_detail', kwargs={'loan_pk': loan_pk}))

    def test_func(self):
        return self.request.user.has_perm('accounts.add_loan')

    def get_amount_to_buyout(self, loan):
        fine = 2.5  # Штраф в день
        expired_days = loan.get_expired_days()
        if expired_days:
            return float(loan.total_amount) * fine * expired_days / 100 + float(loan.total_amount)
        return loan.total_amount

    def record_operation(self, loan):
        Operation.objects.create(
            employee=self.request.user,
            amount=self.get_amount_to_buyout(loan),
            loan=loan,
            operation_type=Operation.TYPE_LOAN_BUYOUT
        )


class LoanProlongationView(UserPassesTestMixin, View):
    def post(self, request, *args, **kwargs):
        prolongation_duration = self.request.POST.get('prolongation_duration')
        prolongation_amount = self.request.POST.get('prolongation_amount')

        self.record_operation(prolongation_amount)

        loan_pk = self.kwargs.get('loan_pk')
        loan = get_object_or_404(Loan, pk=loan_pk)
        loan.duration += int(prolongation_duration)
        loan.date_of_expire = self._get_extended_date_of_expire(loan.date_of_expire, prolongation_duration)
        loan.save()

        messages.add_message(self.request, messages.SUCCESS,
                             f'Залог успешно продлен на {prolongation_duration} дней (до {loan.date_of_expire.strftime("%m.%d.%Y")})')
        return redirect(reverse('pawnshop:loan_detail', kwargs={'loan_pk': loan_pk}))

    def _get_extended_date_of_expire(self, old_date, duration):
        return old_date + timedelta(int(duration))

    def test_func(self):
        return self.request.user.has_perm('accounts.add_loan')

    def get_amount_to_buyout(self, loan):
        fine = 2.5  # Штраф в день
        expired_days = loan.get_expired_days()
        if expired_days:
            return float(loan.total_amount) * fine * expired_days / 100

    def record_operation(self, prolongation_amount):
        loan = get_object_or_404(Loan, pk=self.kwargs.get('loan_pk'))

        if loan.status == Loan.STATUS_EXPIRED:
            prolongation_amount = float(prolongation_amount) + self.get_amount_to_buyout(loan)

        Operation.objects.create(
            employee=self.request.user,
            amount=prolongation_amount,
            loan=loan,
            operation_type=Operation.TYPE_LOAN_PROLONGATION
        )


class LoanProlongationCalculateAjaxView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode())
        duration = data.get('duration')
        payload = {}
        if self.is_duration_valid(duration):
            payload['amount'] = self.get_prolongation_amount(duration)
        else:
            payload['amount'] = None
        return JsonResponse(data=payload)

    @staticmethod
    def is_duration_valid(duration):
        MIN_DURATION = 5
        MAX_DURATION = 30
        if MIN_DURATION <= int(duration) <= MAX_DURATION:
            return True
        return False

    def get_prolongation_amount(self, duration):
        loan = get_object_or_404(Loan, pk=self.kwargs.get('loan_pk'))
        interest_rate = loan.pledge_items.first().category.interest_rate
        return (loan.total_amount * interest_rate * int(duration)) / 100
