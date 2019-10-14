import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import *
from django import forms

from ..models import *


class CriteriaValueCreateView(View):
    def get(self, request, *args, **kwargs):
        pledge_item = get_object_or_404(PledgeItem, pk=self.kwargs.get('pledge_item_pk'))
        criteria_list = pledge_item.category.criteria_list.all()

        context = {
            'client_pk': self.kwargs.get('client_pk'),
            'pledge_item_pk': self.kwargs.get('pledge_item_pk'),
            'criteria_list': criteria_list
        }

        return render(request, 'criteria_value/create.html', context=context)

    def post(self, request, *args, **kwargs):
        data = self.request.body.decode()
        criteria_value_list = json.loads(data).get('criteria')
        for criteria_pk, value in criteria_value_list.items():
            CriteriaValue.objects.create(
                pledge_item=get_object_or_404(PledgeItem, pk=self.kwargs.get('pledge_item_pk')),
                criteria=get_object_or_404(Criteria, pk=criteria_pk),
                value=value
            )

        data = {
            'ok': True
        }
        return JsonResponse(data=data)


class CriteriaValueCreateAjaxView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode())
        pledge_item = get_object_or_404(PledgeItem, pk=int(data.get('pledge_item_pk')))

        for criteria_pk, criteria_value in data.get('criteria_value_list').items():
            pledge_item.criteria_values.create(
                criteria=get_object_or_404(Criteria, pk=criteria_pk),
                value=criteria_value
            )

        return JsonResponse(data={'result': 'ok'})


class CriteriaListAjaxView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'criteria_list': []
        }

        category_pk = self.request.GET.get('category_pk')
        criteria_list = get_object_or_404(Category, pk=category_pk).criteria_list.all()
        for criteria in criteria_list:
            data['criteria_list'].append({
                'pk': criteria.pk,
                'name': criteria.name,
            })

        return JsonResponse(data=data)
