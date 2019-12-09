from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from ..models import Operation


class OperationListView(UserPassesTestMixin, ListView):
    template_name = 'operation/list.html'
    context_object_name = 'operations'
    model = Operation
    ordering = ['-created_at']

    def test_func(self):
        return self.request.user.has_perm('accounts.operations_view')
