from django import forms
from .models import *


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = []


class ConfirmDocumentForm(forms.ModelForm):
    class Meta:
        model = ConfirmDocument
        exclude = ['client']


class PledgeItemForm(forms.ModelForm):
    class Meta:
        model = PledgeItem
        exclude = []
