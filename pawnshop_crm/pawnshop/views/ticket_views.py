from django.http import HttpResponse, FileResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import View
from weasyprint import HTML

from ..models import Loan


class TicketDownloadView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'loan': get_object_or_404(Loan, pk=kwargs.get('loan_pk'))
        }
        rendered_ticket = render_to_string('ticket/ticket.html', context=context)
        response = HttpResponse(content_type="application/pdf")
        HTML(string=rendered_ticket).write_pdf(response)
        return response
