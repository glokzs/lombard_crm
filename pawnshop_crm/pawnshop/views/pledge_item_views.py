import json

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

        return JsonResponse(data)
