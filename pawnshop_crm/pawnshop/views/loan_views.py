from django.http import JsonResponse
from django.views.generic.base import View


class LoanCalculateAjaxView(View):

    def get(self, request, *args, **kwargs):
        requested_amount = int(self.request.GET.get('requested_amount'))
        duration = int(self.request.GET.get('duration'))
        interest_rate = 0.9
        total_amount = round(requested_amount * 100 / (99 - (duration * interest_rate)))

        return JsonResponse({"total_amount": total_amount})
