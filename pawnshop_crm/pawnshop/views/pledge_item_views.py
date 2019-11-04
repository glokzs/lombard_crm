import json
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import *

from ..models import *
from ..forms import *


class PledgeItemCreateView(CreateView):
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


class PledgeItemCreateAjaxView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode())
        pledge_item = PledgeItem.objects.create(
            category=get_object_or_404(Category, pk=int(data.get('category_pk'))),
            subcategory=get_object_or_404(Subcategory, pk=int(data.get('subcategory_pk'))),
            name=data.get('name'),
            price=data.get('price'),
            description=data.get('description'),
            note=data.get('note'),
        )

        data = {
            'pledge_item': {
                'pk': pledge_item.pk,
                'name': pledge_item.name,
                'price': pledge_item.price,
            }
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
        return JsonResponse(data)


class PledgeItemListView(ListView):
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
