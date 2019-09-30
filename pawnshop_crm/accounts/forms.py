from django import forms

from accounts.models import User

USER_TYPES = [
    ("не указана", "Выберите тип прав"),
    ("Администратор", "Администратор"),
    ("Кассир-оценщик", "Кассир-оценщик"),
    ("Аудитор", "Аудитор")
]


class UserForm(forms.ModelForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите логин'
        })
    )
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
    user_type = forms.ChoiceField(
        label='Должность',
        choices=USER_TYPES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'email']
