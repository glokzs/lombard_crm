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


def _get_category_choices():
    category_choices = [
        ['', 'Выберите категорию']
    ]
    categories = Category.objects.all()
    for category in categories:
        category_choices.append([category.pk, category.name])
    return category_choices


class PledgeItemForm(forms.ModelForm):
    name = forms.CharField(
        label='Название',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        })
    )
    price = forms.DecimalField(
        label='Оценочная стоимость',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите оценочную стоимость (тенге)'
        })
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })
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
    category = forms.ChoiceField(
        label='Категория',
        choices=_get_category_choices(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Выберите категорию'
        })
    )

    class Meta:
        model = PledgeItem
        exclude = ['subcategory']
