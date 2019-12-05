import json
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, View, ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from ..models import PledgeItem, Category, Subcategory, Loan
from ..forms import PledgeItemCreateForm


class PledgeItemCreateView(UserPassesTestMixin, CreateView):
    template_name = 'pledge_item/create.html'
    model = PledgeItem
    form_class = PledgeItemCreateForm

    def get_context_data(self, **kwargs):
        client_pk = self.kwargs.get('client_pk')
        kwargs['client_pk'] = client_pk
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        category_pk = int(self.request.POST.get('category'))
        subcategory_pk = int(self.request.POST.get('subcategory'))
        form.instance.category = get_object_or_404(Category, pk=category_pk)
        form.instance.subcategory = get_object_or_404(Subcategory, pk=subcategory_pk)
        return super().form_valid(form)

    def get_success_url(self):
        client_pk = self.kwargs.get('client_pk')
        pledge_item_pk = self.object.pk
        kwargs = {
            'client_pk': client_pk,
            'pledge_item_pk': pledge_item_pk
        }
        return reverse('pawnshop:criteria_value_create', kwargs=kwargs)

    def test_func(self):
        return self.request.user.has_perm('accounts.loan_item_list_view')


class PledgeItemCreateAjaxView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode())

        payload = {}
        invalid_fields = self.get_invalid_fields(data)
        if invalid_fields:
            payload['errors'] = invalid_fields
        else:
            pledge_item = PledgeItem.objects.create(
                category=get_object_or_404(Category, pk=int(data.get('category_pk'))),
                subcategory=get_object_or_404(Subcategory, pk=int(data.get('subcategory_pk'))),
                name=data.get('name'),
                price=data.get('price'),
                description=data.get('description'),
                note=data.get('note'),
            )
            payload['pledge_item'] = {
                'pk': pledge_item.pk,
                'name': pledge_item.name,
                'price': pledge_item.price,
            }
            if not self.request.session.get('pledge_item_list'):
                self.request.session['pledge_item_list'] = []
            self.request.session['pledge_item_list'].append({
                'pk': str(pledge_item.pk),
                'name': pledge_item.name,
                'price': pledge_item.price,
                'interest_rate': str(pledge_item.category.interest_rate)
            })
            self.request.session.save()
        return JsonResponse(payload)

    def get_invalid_fields(self, data):
        invalid_fields = []
        if not data.get('name'):
            invalid_fields.append('id_name')
        if not data.get('price'):
            invalid_fields.append('id_price')
        if not data.get('description'):
            invalid_fields.append('id_description')
        return invalid_fields


class PledgeItemListView(UserPassesTestMixin, ListView):
    template_name = 'pledge_item/list.html'
    context_object_name = 'pledge_items'
    model = PledgeItem

    def get_context_data(self, **kwargs):
        VALUE_IF_NONE = 0
        total_amount = Loan.objects.aggregate(sum=Sum("total_amount"))['sum']
        kwargs['total_amount'] = total_amount if total_amount else VALUE_IF_NONE
        client_amount = Loan.objects.aggregate(sum=Sum("client_amount"))['sum']
        kwargs['client_amount'] = client_amount if client_amount else VALUE_IF_NONE
        return super().get_context_data(**kwargs)

    def test_func(self):
        return self.request.user.has_perm('accounts.loan_item_list_view')
