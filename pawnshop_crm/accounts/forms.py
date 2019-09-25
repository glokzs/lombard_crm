from django import forms

from accounts.models import User

USER_TYPES = [
        ("0", "Выберите тип прав"),
        ("1", "Администратор"),
        ("2", "Кассир_оценщик"),
        ("3", "Аудитор")
        ]

class UserForm(forms.ModelForm):
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
        choices = USER_TYPES,
        required=True,
        widget=forms.Select()
    )
    # birth_date = forms.DateField(
    #     label='Дата рождения',
    #     widget=forms.SelectDateWidget
    # )
    # location = forms.CharField(
    #     label='Населенный пункт',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите название населенного пункта'
    #     })
    # )
    # street = forms.CharField(
    #     label='Улица',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите название улицы'
    #     })
    # )
    # house_number = forms.CharField(
    #     label='Номер дома',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите номер дома'
    #     })
    # )
    # apartment_number = forms.CharField(
    #     label='Номер квартиры',
    #     required=False,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите номер квартиры'
    #     })
    # )
    # actual_address = forms.CharField(
    #     label='Фактический адрес проживания',
    #     required=False,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите фактический адрес проживания'
    #     })
    # )
    # birth_place = forms.CharField(
    #     label='Место рождения',
    #     required=False,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите место рождения'
    #     })
    # )

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
    # citizenship = forms.CharField(
    #     label='Гражданство',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите гражданство'
    #     })
    # )
    # files = forms.FileField(
    #     label='Файлы',
    #     required=False,
    #     widget=forms.FileInput(
    #         attrs={
    #             'class': 'form-control-file',
    #         }
    #     )
    # )

    class Meta:
        model = User
        exclude = []
