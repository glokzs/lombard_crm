from django import forms
from ..models import *


class ConfirmDocumentForm(forms.ModelForm):
    DOCUMENT_TYPE_CHOICES = [
        ['Удостоверение', 'Удостоверение'],
        ['Паспорт', 'Паспорт'],
    ]

    document_type = forms.ChoiceField(
        label='Тип документа',
        required=True,
        choices=DOCUMENT_TYPE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    iin = forms.CharField(
        label='ИИН',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ИИН'
        })
    )
    serial_number = forms.CharField(
        label='Серийный номер',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите серийный номер'
        })
    )

    GIVEN_BY_CHOICES = [
        ['МВД РК', 'МВД РК']
    ]

    given_by = forms.ChoiceField(
        label='Выдан кем',
        required=True,
        choices=GIVEN_BY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    given_at = forms.DateField(
        label='Дата выдачи',
        required=True,
        widget=forms.SelectDateWidget
    )
    note = forms.CharField(
        label='Примечание',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите примечание'
        })
    )
    image = forms.ImageField(
        label='Фотография',
        widget=forms.FileInput(attrs={
            'class': 'form-control-file',
        })
    )

    class Meta:
        model = ConfirmDocument
        exclude = ['client']
