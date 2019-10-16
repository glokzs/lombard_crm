import os
import pdfkit

from django.views.generic import *
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from ..models import *


# def ticket_download_view(request):
#     # html = render(request, 'ticket/ticket.html')
#     # file_path = os.path.join(settings.MEDIA_ROOT, 'ticket.pdf')
#     # pdfkit.from_string(html.content.decode(), file_path)
#     return render(request, 'ticket/ticket.html')


class TicketDownloadView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'loan': get_object_or_404(Loan, pk=self.kwargs.get('loan_pk'))
        }

        return render(request, 'ticket/ticket.html', context)
