from django.contrib import admin

from .models import User, Client, ConfirmDocument

admin.site.register(User)
admin.site.register(Client)
admin.site.register(ConfirmDocument)
