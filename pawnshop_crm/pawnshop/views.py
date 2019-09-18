from django.shortcuts import render
from django.views.generic import *


class CreditListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'credit/list.html')


class CreditCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'credit/create.html')

