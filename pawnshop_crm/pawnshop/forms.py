from django import forms
from .models import *


class ClientForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите фамилию'
        })
    )
    middle_name = forms.CharField(
        label='Отчество',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите отчество'
        })
    )
    birth_date = forms.DateField(
        label='Дата рождения',
        widget=forms.SelectDateWidget
    )
    location = forms.CharField(
        label='Населенный пункт',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название населенного пункта'
        })
    )
    street = forms.CharField(
        label='Улица',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название улицы'
        })
    )
    house_number = forms.CharField(
        label='Номер дома',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите номер дома'
        })
    )
    apartment_number = forms.CharField(
        label='Номер квартиры',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите номер квартиры'
        })
    )
    actual_address = forms.CharField(
        label='Фактический адрес проживания',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите фактический адрес проживания'
        })
    )
    birth_place = forms.CharField(
        label='Место рождения',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите место рождения'
        })
    )
    phone = forms.CharField(
        label='Номер телефона',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите номер телефона'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email'
        })
    )
    citizenship = forms.CharField(
        label='Гражданство',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите гражданство'
        })
    )
    files = forms.FileField(
        label='Файлы',
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control-file',
            }
        )
    )

    class Meta:
        model = Client
        exclude = []


class ConfirmDocumentForm(forms.ModelForm):
    DOCUMENT_TYPE_CHOICES = [
        ['Удостоверение', 'Удостоверение'],
        ['Паспорт', 'Паспорт'],
    ]

    document_type = forms.ChoiceField(
        label='Тип документа',
        choices=DOCUMENT_TYPE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    iin = forms.CharField(
        label='ИИН',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ИИН'
        })
    )
    serial_number = forms.CharField(
        label='Серийный номер',
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
        choices=GIVEN_BY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    given_at = forms.DateField(
        label='Дата выдачи',
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
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите примечание'
        })
    )
    image = forms.ImageField(
        label='Фотография',
        required=False,
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
