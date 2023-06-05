import django_filters
from django import forms

from apps.catalog.models import Companies, Workers
from apps.personal.models import LogActs, LogContract, LogAddAgreements, LogOrdersK, LogOrdersLS, LogOrdersSh, \
    LogWorkContracts, RegisterFinSupport


class LogActsFilter(django_filters.FilterSet):
    log_acts_year = django_filters.NumberFilter(field_name='date__year', lookup_expr='exact',
                                                widget=forms.Select(attrs={'class': 'dropdown'},
                                                                    choices=[(2023, 2023), (2024, 2024)]),
                                                validators=[lambda y: y in [2023, 2024]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = LogActs
        fields = ['log_acts_year', 'company']


class LogContractFilter(django_filters.FilterSet):
    log_contract_year = django_filters.NumberFilter(field_name='date__year', lookup_expr='exact',
                                                    widget=forms.Select(attrs={'class': 'dropdown'},
                                                                        choices=[(2023, 2023), (2024, 2024)]),
                                                    validators=[lambda y: y in [2023, 2024]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = LogContract
        fields = ['log_contract_year', 'company']


class LogAddAgreementsFilter(django_filters.FilterSet):
    log_add_agreements_year = django_filters.NumberFilter(field_name='date__year', lookup_expr='exact',
                                                          widget=forms.Select(attrs={'class': 'dropdown'},
                                                                              choices=[(2023, 2023), (2024, 2024)]),
                                                          validators=[lambda y: y in [2023, 2024]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = LogAddAgreements
        fields = ['log_add_agreements_year', 'company']


class LogOrdersKFilter(django_filters.FilterSet):
    log_orders_K_year = django_filters.NumberFilter(field_name='date__year', lookup_expr='exact',
                                                    widget=forms.Select(attrs={'class': 'dropdown'},
                                                                        choices=[(2023, 2023), (2024, 2024)]),
                                                    validators=[lambda y: y in [2023, 2024]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))
    worker = django_filters.ModelChoiceFilter(queryset=Workers.objects.all(), empty_label="Все сотрудники",
                                              widget=forms.Select(attrs={'class': 'dropdown'}))
    reason = django_filters.ChoiceFilter(choices=[r for r in LogOrdersK.REASON_TYPES if r[0] != ' '],
                                         empty_label="Все причины", widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = LogOrdersK
        fields = ['log_orders_K_year', 'company', 'worker', 'reason']


class LogOrdersLSFilter(django_filters.FilterSet):
    log_orders_LS_year = django_filters.NumberFilter(field_name='date__year', lookup_expr='exact',
                                                     widget=forms.Select(attrs={'class': 'dropdown'},
                                                                         choices=[(2023, 2023), (2024, 2024)]),
                                                     validators=[lambda y: y in [2023, 2024]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))
    worker = django_filters.ModelChoiceFilter(queryset=Workers.objects.all(), empty_label="Все сотрудники",
                                              widget=forms.Select(attrs={'class': 'dropdown'}))
    reason = django_filters.ChoiceFilter(choices=LogOrdersLS.REASON_TYPES, empty_label="Все причины",
                                         widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = LogOrdersLS
        fields = ['log_orders_LS_year', 'company', 'worker', 'reason']


class LogOrdersShFilter(django_filters.FilterSet):
    log_orders_Sh_year = django_filters.NumberFilter(field_name='date__year', lookup_expr='exact',
                                                     widget=forms.Select(attrs={'class': 'dropdown'},
                                                                         choices=[(2023, 2023), (2024, 2024)]),
                                                     validators=[lambda y: y in [2023, 2024]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = LogOrdersSh
        fields = ['log_orders_Sh_year', 'company']


class LogWorkContractsFilter(django_filters.FilterSet):
    log_work_contracts_year = django_filters.NumberFilter(field_name='date__year', lookup_expr='exact',
                                                          widget=forms.Select(attrs={'class': 'dropdown'},
                                                                              choices=[(2023, 2023), (2024, 2024)]),
                                                          validators=[lambda y: y in [2023, 2024]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = LogWorkContracts
        fields = ['log_work_contracts_year', 'company']


class RegisterFinSupportFilter(django_filters.FilterSet):
    register_fin_support_year = django_filters.NumberFilter(field_name='date_of_document__year', lookup_expr='exact',
                                                            widget=forms.Select(attrs={'class': 'dropdown'},
                                                                                choices=[(2023, 2023), (2024, 2024)]),
                                                            validators=[lambda y: y in [2023, 2024]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))
    worker = django_filters.ModelChoiceFilter(queryset=Workers.objects.filter(fired='нет'), empty_label="Все сотрудники",
                                              widget=forms.Select(attrs={'class': 'dropdown'}))
    month_of_issue = django_filters.ChoiceFilter(choices=RegisterFinSupport.MONTH_TYPES, empty_label="Все месяцы",
                                                 widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = RegisterFinSupport
        fields = ['register_fin_support_year', 'company', 'worker', 'month_of_issue']
