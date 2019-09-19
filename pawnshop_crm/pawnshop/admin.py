from django.contrib import admin
from .models import Client, ConfirmDocument, Category


admin.site.register(Client)
admin.site.register(ConfirmDocument)
admin.site.register(Category)
