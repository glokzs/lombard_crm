from django import forms
from django.shortcuts import get_object_or_404

from ..models import *


class LoanCreateForm(forms.ModelForm):
    client_amount = forms.DecimalField(
        label='Запрашиваемая сумма',
        max_digits=20,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите запрашиваемую сумму'
        })
    )
    duration = forms.IntegerField(
        label='Срок займа',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '5',
            'max': '30',
            'placeholder': 'Введите срок займа'
        })
    )

    total_amount = forms.DecimalField(
        label='Общая сумма займа',
        required=True,
        max_digits=8,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly',
            'placeholder': 'Здесь выведется общая сумма займа'
        })
    )

    class Meta:
        model = Loan
        exclude = ['client', 'pledge_item', 'date_of_expire', 'total_amount']
