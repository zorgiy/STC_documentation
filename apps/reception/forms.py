from django import forms
from django.forms import ModelForm, TextInput, DateInput, Textarea
from django_select2.forms import Select2Widget

from apps.catalog.models import Partners, Companies, Workers
from apps.reception.models import Incoming, Outgoing, Order


class IncomingForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))
    client = forms.ModelChoiceField(queryset=Partners.objects.all(), label='Контрагент', empty_label="",
                                    widget=Select2Widget(attrs={'class': 'form-control partners-select2',
                                                                'data-minimum-input-length': 2}))
    author = forms.ModelChoiceField(queryset=Workers.objects.filter(fired='нет'), label='Исполнитель', empty_label="",
                                    widget=Select2Widget(attrs={'class': 'form-control author-select2'}))

    class Meta:
        model = Incoming
        fields = '__all__'
        exclude = ('index', 'author_created')
        widgets = {
            'receipt_date': DateInput(attrs={'class': 'form-control',
                                             'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'document_number': TextInput(attrs={'class': 'form-control'}),
            'document_date': DateInput(attrs={'class': 'form-control',
                                              'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'summary': Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'type_of_receipt': forms.Select(attrs={'class': 'form-select mb-2',
                                                   'style': 'display: inline-block; width: auto'}),
            'execution_control': forms.Select(attrs={'class': 'form-select',
                                                     'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['document_number'].label = ''
        self.fields['summary'].label = ''
        self.fields['document_number'].widget.attrs['placeholder'] = '№ документа'
        self.fields['summary'].widget.attrs['placeholder'] = 'Краткое содержание'


class OutgoingForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))
    client = forms.ModelChoiceField(queryset=Partners.objects.all(), label='Контрагент', empty_label="",
                                    widget=Select2Widget(attrs={'class': 'form-control partners-select2',
                                                                'data-minimum-input-length': 2}))
    signed = forms.ModelChoiceField(queryset=Workers.objects.filter(fired='нет'), label='Подписал', empty_label="",
                                    widget=Select2Widget(attrs={'class': 'form-control signed-select2'}))
    author = forms.ModelChoiceField(queryset=Workers.objects.filter(fired='нет'), label='Исполнитель', empty_label="",
                                    widget=Select2Widget(attrs={'class': 'form-control author-select2'}))

    class Meta:
        model = Outgoing
        fields = '__all__'
        exclude = ('index', 'author_created')
        widgets = {
            'receipt_date': DateInput(attrs={'class': 'form-control',
                                             'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'summary': Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'type_of_receipt': forms.Select(attrs={'class': 'form-select mb-2',
                                                   'style': 'display: inline-block; width: auto'}),
            'execution_control': forms.Select(attrs={'class': 'form-select mb-2',
                                                     'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['summary'].label = ''
        self.fields['summary'].widget.attrs['placeholder'] = 'Краткое содержание'


class OrderForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))
    author = forms.ModelChoiceField(queryset=Workers.objects.filter(fired='нет'), label='Исполнитель', empty_label="",
                                    widget=Select2Widget(attrs={'class': 'form-control author-select2'}))

    class Meta:
        model = Order
        fields = "__all__"
        exclude = ('number', 'author_created')
        widgets = {
            'date': DateInput(attrs={'class': 'form-control',
                                     'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'summary': Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'additional_authors': forms.Select(attrs={'class': 'form-select mb-2',
                                                      'style': 'display: inline-block; width: auto'}),
            'period_of_execution': DateInput(attrs={'class': 'form-control',
                                                    'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'execution_control': forms.Select(attrs={'class': 'form-select mb-2',
                                                     'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['summary'].label = ''
        self.fields['author'].label = ''
        self.fields['summary'].widget.attrs['placeholder'] = 'Краткое содержание'
