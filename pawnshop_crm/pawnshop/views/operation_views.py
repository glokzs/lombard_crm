from django.db.models import Sum
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from ..models import Operation


class OperationListView(UserPassesTestMixin, ListView):
    template_name = 'operation/list.html'
    context_object_name = 'operations'
    model = Operation
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        VALUE_IF_NONE = 0

        total_amount = Operation.objects.aggregate(sum=Sum("amount"))['sum']
        kwargs['total_amount'] = total_amount if total_amount else VALUE_IF_NONE

        return super().get_context_data(**kwargs)

    def test_func(self):
        return self.request.user.has_perm('accounts.operations_view')