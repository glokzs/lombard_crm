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
