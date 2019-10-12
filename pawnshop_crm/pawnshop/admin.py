from django.contrib import admin

from .models import *


admin.site.register(Client)
admin.site.register(ConfirmDocument)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Criteria)
admin.site.register(CriteriaValue)
admin.site.register(PledgeItem)
admin.site.register(Loan)
admin.site.register(FakeOperation)
admin.site.register(Contract)

admin.site.site_header = 'Lombard CRM'
