from django import forms
from django.forms import ModelForm, TextInput, DateInput, Textarea
from django_select2.forms import Select2Widget

from apps.catalog.models import Companies, Workers
from apps.personal.models import LogActs, LogContract, LogAddAgreements, LogOrdersK, LogOrdersLS, LogOrdersSh, \
    LogWorkContracts, RegisterFinSupport


class LogActsForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))
    worker = forms.ModelChoiceField(queryset=Workers.objects.all(), label='Сотрудник', empty_label='',
                                    widget=Select2Widget(attrs={'class': 'form-control workers-select2'}))

    class Meta:
        model = LogActs
        fields = '__all__'
        exclude = ('author_created',)
        widgets = {
            'act_number': TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control',
                                     'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'cause': Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'compiler': forms.Select(attrs={'class': 'form-select mb-2',
                                            'style': 'display: inline-block; width: auto'}),
            'period': Textarea(attrs={'class': 'form-control', 'rows': '1'}),
            'execution_mark': TextInput(attrs={'class': 'form-control'}),
            'result': TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select mb-2', 'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['act_number'].label = ''
        self.fields['worker'].label = ''
        self.fields['cause'].label = ''
        self.fields['period'].label = ''
        self.fields['execution_mark'].label = ''
        self.fields['result'].label = ''
        self.fields['act_number'].widget.attrs['placeholder'] = '№ акта'
        self.fields['cause'].widget.attrs['placeholder'] = 'Причина составления акта'
        self.fields['period'].widget.attrs['placeholder'] = 'Период'
        self.fields['execution_mark'].widget.attrs['placeholder'] = 'Отметка об исполнении'
        self.fields['result'].widget.attrs['placeholder'] = 'Результат'


class LogContractForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))
    worker = forms.ModelChoiceField(queryset=Workers.objects.all(), label='Сотрудник', empty_label='',
                                    widget=Select2Widget(attrs={'class': 'form-control workers-select2'}))

    class Meta:
        model = LogContract
        fields = '__all__'
        exclude = ('author_created',)
        widgets = {
            'number': TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control',
                                     'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'content': Textarea(attrs={'class': 'form-control', 'rows': '1'}),
            'act_number': TextInput(attrs={'class': 'form-control'}),
            'act_date': DateInput(attrs={'class': 'form-control',
                                         'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select mb-2', 'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['number'].label = ''
        self.fields['worker'].label = ''
        self.fields['content'].label = ''
        self.fields['act_number'].label = ''
        self.fields['number'].widget.attrs['placeholder'] = '№'
        self.fields['content'].widget.attrs['placeholder'] = 'Содержание'
        self.fields['act_number'].widget.attrs['placeholder'] = '№ акта'


class LogAddAgreementsForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))
    worker = forms.ModelChoiceField(queryset=Workers.objects.filter(fired='нет'), label='Сотрудник', empty_label='',
                                    widget=Select2Widget(attrs={'class': 'form-control workers-select2'}))

    class Meta:
        model = LogAddAgreements
        fields = '__all__'
        exclude = ('author_created',)
        widgets = {
            'number': TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control',
                                     'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'content': Textarea(attrs={'class': 'form-control', 'rows': '1'}),
            'contract_number': TextInput(attrs={'class': 'form-control'}),
            'contract_date': DateInput(attrs={'class': 'form-control',
                                              'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select',
                                          'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['number'].label = ''
        self.fields['worker'].label = ''
        self.fields['content'].label = ''
        self.fields['contract_number'].label = ''
        self.fields['number'].widget.attrs['placeholder'] = '№'
        self.fields['content'].widget.attrs['placeholder'] = 'Содержание'
        self.fields['contract_number'].widget.attrs['placeholder'] = '№ трудового договора'


class LogOrdersKForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))
    worker = forms.ModelChoiceField(queryset=Workers.objects.filter(fired='нет'), label='Сотрудник', empty_label='',
                                    widget=Select2Widget(attrs={'class': 'form-control workers-select2'}))

    class Meta:
        model = LogOrdersK
        fields = '__all__'
        exclude = ('author_created',)
        widgets = {
            'number': TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control',
                                     'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'reason': forms.Select(attrs={'class': 'form-select mb-2', 'style': 'display: inline-block; width: auto'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': '1'}),
            'period': Textarea(attrs={'class': 'form-control', 'rows': '1'}),
            'status': forms.Select(attrs={'class': 'form-select', 'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['number'].label = ''
        self.fields['worker'].label = ''
        self.fields['description'].label = ''
        self.fields['period'].label = ''
        self.fields['number'].widget.attrs['placeholder'] = '№'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание'
        self.fields['period'].widget.attrs['placeholder'] = 'Период'


class LogOrdersLSForm(LogOrdersKForm):
    worker = forms.ModelChoiceField(queryset=Workers.objects.all(), label='Сотрудник', empty_label='',
                                    widget=Select2Widget(attrs={'class': 'form-control workers-select2'}))

    class Meta(LogOrdersKForm.Meta):
        model = LogOrdersLS
        fields = '__all__'


class LogOrdersShForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))

    class Meta:
        model = LogOrdersSh
        fields = '__all__'
        exclude = ('author_created',)
        widgets = {
            'number': TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control',
                                     'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'content': Textarea(attrs={'class': 'form-control', 'rows': '1'}),
            'period': Textarea(attrs={'class': 'form-control', 'rows': '1'}),
            'status': forms.Select(attrs={'class': 'form-select', 'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['number'].label = ''
        self.fields['content'].label = ''
        self.fields['period'].label = ''
        self.fields['number'].widget.attrs['placeholder'] = '№'
        self.fields['content'].widget.attrs['placeholder'] = 'Содержание'
        self.fields['period'].widget.attrs['placeholder'] = 'Период'


class LogWorkContractsForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))
    worker = forms.ModelChoiceField(queryset=Workers.objects.all(), label='Сотрудник', empty_label='',
                                    widget=Select2Widget(attrs={'class': 'form-control workers-select2'}))

    class Meta:
        model = LogWorkContracts
        fields = '__all__'
        exclude = ('author_created',)
        widgets = {
            'number': TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control',
                                     'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'position_division': Textarea(attrs={'class': 'form-control', 'rows': '1'}),
            'contract_type': forms.Select(attrs={'class': 'form-select mb-2',
                                                 'style': 'display: inline-block; width: auto'}),
            'status': forms.Select(attrs={'class': 'form-select', 'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['number'].label = ''
        self.fields['worker'].label = ''
        self.fields['position_division'].label = ''
        self.fields['number'].widget.attrs['placeholder'] = '№'
        self.fields['position_division'].widget.attrs['placeholder'] = 'Должность/подразделение'


class RegisterFinSupportForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Выберите компанию",
                                     widget=forms.Select(attrs={'class': 'form-select mb-2'}))
    worker = forms.ModelChoiceField(queryset=Workers.objects.filter(fired='нет'), label='Сотрудник', empty_label='',
                                    widget=Select2Widget(attrs={'class': 'form-control workers-select2'}))

    class Meta:
        model = RegisterFinSupport
        fields = '__all__'
        exclude = ('date_of_document', 'author_created')
        widgets = {
            'position': TextInput(attrs={'class': 'form-control'}),
            'date_of_receipt': DateInput(attrs={'class': 'form-control',
                                                'style': 'display: inline-block; width: auto', 'type': 'date'}),
            'group': forms.Select(attrs={'class': 'form-select', 'style': 'display: inline-block; width: auto'}),
            'amount': forms.Select(attrs={'class': 'form-select mb-2', 'style': 'display: inline-block; width: auto'}),
            'month_of_issue': forms.Select(attrs={'class': 'form-select mb-2',
                                                  'style': 'display: inline-block; width: auto'}),
            'comments': TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select', 'style': 'display: inline-block; width: auto'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].label = ''
        self.fields['worker'].label = ''
        self.fields['position'].label = ''
        self.fields['comments'].label = ''
        self.fields['position'].widget.attrs['placeholder'] = 'Должность'
        self.fields['comments'].widget.attrs['placeholder'] = 'Комментарии'
