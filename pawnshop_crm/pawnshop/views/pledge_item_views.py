from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *

from ..models import *
from ..forms import *


class PledgeItemCreateView(CreateView):
    template_name = 'pledge_item/create.html'
    model = PledgeItem
    form_class = PledgeItemForm

    def get_success_url(self):
        return reverse('pawnshop:credit_list')
