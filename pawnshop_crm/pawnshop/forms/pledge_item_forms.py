from django import forms
from ..models import PledgeItem, Category


def _get_category_choices():
    category_choices = [
        ['', 'Выберите категорию']
    ]
    try:
        categories = Category.objects.all()

        for category in categories:
            category_choices.append([category.pk, category.name])
        return category_choices
    except BaseException:
        return []


class PledgeItemCreateForm(forms.ModelForm):
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
        fields = ['name', 'price', 'description', 'note', 'image']
        exclude = ['subcategory', 'category']
