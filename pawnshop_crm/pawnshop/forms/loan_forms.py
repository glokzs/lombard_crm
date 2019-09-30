from django import forms
from ..models import *


class LoanCreateForm(forms.ModelForm):
    client_amount = forms.DecimalField(
        label='Запрашиваемая сумма',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': ''
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
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            # 'disabled': 'true',
        })
    )

    class Meta:
        model = Loan
        exclude = ['client', 'pledge_item', 'date_of_expire']
