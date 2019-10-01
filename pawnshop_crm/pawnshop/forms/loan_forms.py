from django import forms
from django.shortcuts import get_object_or_404

from ..models import *


class LoanCreateForm(forms.ModelForm):
    client_amount = forms.DecimalField(
        label='Запрашиваемая сумма',
        max_digits=8,
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

    # def clean_total_amount(self, client_amount, duration):
    #     pledge_item_pk = self.request.session.get('pledge_item_pk')
    #     interest_rate = get_object_or_404(PledgeItem, pk=pledge_item_pk).category.interest_rate
    #     total_amount_check = 100 * client_amount / (99 - interest_rate * duration)
    #     total_amount = self.cleaned_data.get("total_amount")
    #     if total_amount and total_amount_check and total_amount != total_amount_check:
    #         raise forms.ValidationError('Общая сумма займа не соответствует')
    #     return total_amount

    class Meta:
        model = Loan
        exclude = ['client', 'pledge_item', 'date_of_expire', 'total_amount']
