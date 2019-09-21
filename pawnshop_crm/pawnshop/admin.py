from django.contrib import admin
from .models import *


admin.site.register(Client)
admin.site.register(ConfirmDocument)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Criteria)
admin.site.register(CriteriaPledgeItem)
admin.site.register(PledgeItem)
