from django import forms
from .models import Client, ConfirmDocument


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = []


class ConfirmDocumentForm(forms.ModelForm):
    class Meta:
        model = ConfirmDocument
        exclude = ['client']
