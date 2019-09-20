from django.contrib import admin
from .models import Client, ConfirmDocument, Category, Subcategory, Criteria


admin.site.register(Client)
admin.site.register(ConfirmDocument)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Criteria)
