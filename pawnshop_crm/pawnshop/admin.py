from django.contrib import admin

from .models import Client, ConfirmDocument, Category, Subcategory, Criteria, CriteriaValue, PledgeItem, Loan, \
    FakeOperation, Operation

admin.site.register(Client)
admin.site.register(ConfirmDocument)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Criteria)
admin.site.register(CriteriaValue)
admin.site.register(PledgeItem)
admin.site.register(Loan)
admin.site.register(FakeOperation)
admin.site.register(Operation)

admin.site.site_header = 'Lombard CRM'
