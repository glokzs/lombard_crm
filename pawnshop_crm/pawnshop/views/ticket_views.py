import os
import pdfkit

from django.views.generic import *
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from ..models import *


class TicketDownloadView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'loan': get_object_or_404(Loan, pk=self.kwargs.get('loan_pk'))
        }

        return render(request, 'ticket/ticket.html', context)
