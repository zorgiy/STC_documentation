from django import forms
from django.forms import ModelForm, TextInput, DateInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from apps.catalog.models import Partners, Companies, Workers


class PartnersForm(ModelForm):
    telephone = PhoneNumberField(region='RU', widget=PhoneNumberPrefixWidget(
        attrs={'class': 'form-control', 'style': 'display: inline-block; width: 50%'},
        initial='RU', country_choices=[('RU''', 'Россия'), ('KZ', 'Казахстан')]), required=False)

    class Meta:
        model = Partners
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'general_director': TextInput(attrs={'class': 'form-control'}),
            'the_contact_person': TextInput(attrs={'class': 'form-control'}),
            'mailing_address': TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['city'].label = ''
        self.fields['telephone'].label = ''
        self.fields['email'].label = ''
        self.fields['general_director'].label = ''
        self.fields['the_contact_person'].label = ''
        self.fields['mailing_address'].label = ''
        self.fields['name'].widget.attrs['placeholder'] = 'Название'
        self.fields['city'].widget.attrs['placeholder'] = 'Город'
        self.fields['telephone'].widget.attrs['placeholder'] = 'Телефон'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['general_director'].widget.attrs['placeholder'] = 'Генеральный директор'
        self.fields['the_contact_person'].widget.attrs['placeholder'] = 'Контактное лицо'
        self.fields['mailing_address'].widget.attrs['placeholder'] = 'Почтовый адрес'


class CompaniesForm(ModelForm):
    telephone = PhoneNumberField(region='RU', widget=PhoneNumberPrefixWidget(
        attrs={'class': 'form-control', 'style': 'display: inline-block; width: 50%'},
        initial='RU', country_choices=[('RU''', 'Россия'), ('KZ', 'Казахстан')]), required=False)

    class Meta:
        model = Companies
        fields = '__all__'
        exclude = ('last_document_number_incoming', 'last_document_number_outgoing', 'last_document_number_order',
                   'last_document_year')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'index': TextInput(attrs={'class': 'form-control'}),
            'mailing_address': TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['index'].label = ''
        self.fields['telephone'].label = ''
        self.fields['mailing_address'].label = ''
        self.fields['name'].widget.attrs['placeholder'] = 'Название'
        self.fields['index'].widget.attrs['placeholder'] = 'Индекс'
        self.fields['telephone'].widget.attrs['placeholder'] = 'Телефон'
        self.fields['mailing_address'].widget.attrs['placeholder'] = 'Почтовый адрес'


class WorkersForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))
    telephone = PhoneNumberField(region='RU', widget=PhoneNumberPrefixWidget(
        attrs={'class': 'form-control', 'style': 'display: inline-block; width: 50%'},
        initial='RU', country_choices=[('RU''', 'Россия'), ('KZ', 'Казахстан')]), required=False)
    cellular = PhoneNumberField(region='RU', widget=PhoneNumberPrefixWidget(
        attrs={'class': 'form-control', 'style': 'display: inline-block; width: 50%'},
        initial='RU', country_choices=[('RU''', 'Россия'), ('KZ', 'Казахстан')]), required=False)

    class Meta:
        model = Workers
        fields = '__all__'
        widgets = {
            'surname': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'second_name': TextInput(attrs={'class': 'form-control'}),
            'birthday': DateInput(attrs={'class': 'form-control',
                                         'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'position': TextInput(attrs={'class': 'form-control'}),
            'internal_telephone': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'fired': forms.Select(attrs={'class': 'form-select', 'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['surname'].label = ''
        self.fields['first_name'].label = ''
        self.fields['second_name'].label = ''
        self.fields['position'].label = ''
        self.fields['telephone'].label = ''
        self.fields['internal_telephone'].label = ''
        self.fields['cellular'].label = ''
        self.fields['email'].label = ''
        self.fields['surname'].widget.attrs['placeholder'] = 'Фамилия'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['second_name'].widget.attrs['placeholder'] = 'Отчество'
        self.fields['position'].widget.attrs['placeholder'] = 'Должность'
        self.fields['telephone'].widget.attrs['placeholder'] = 'Телефон'
        self.fields['internal_telephone'].widget.attrs['placeholder'] = 'Внутренний телефон'
        self.fields['cellular'].widget.attrs['placeholder'] = 'Сотовый телефон'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
