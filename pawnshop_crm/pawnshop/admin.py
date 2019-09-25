from django.contrib import admin

from .models import *

class LoanViewAdmin(admin.ModelAdmin):
    list_display = ('client', 'pledge_item', 'total_amount')



admin.site.register(Client)
admin.site.register(ConfirmDocument)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Criteria)
admin.site.register(CriteriaPledgeItem)
admin.site.register(PledgeItem)
admin.site.register(Loan, LoanViewAdmin)


admin.site.site_header = 'Lombard CRM'