import django_filters
from django import forms

from apps.catalog.models import Partners, Companies
from apps.reception.models import Incoming, Outgoing, Order


class IncomingFilter(django_filters.FilterSet):
    incoming_year = django_filters.NumberFilter(field_name='receipt_date__year', lookup_expr='exact',
                                                widget=forms.Select(attrs={'class': 'dropdown'},
                                                                    choices=[(2023, 2023), (2022, 2022)]),
                                                validators=[lambda y: y in [2023, 2022]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))
    client = django_filters.ModelChoiceFilter(queryset=Partners.objects.all(), empty_label="Все контрагенты",
                                              widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = Incoming
        fields = ['incoming_year', 'company', 'client']


class OutgoingFilter(django_filters.FilterSet):
    outgoing_year = django_filters.NumberFilter(field_name='receipt_date__year', lookup_expr='exact',
                                                widget=forms.Select(attrs={'class': 'dropdown'},
                                                                    choices=[(2023, 2023), (2022, 2022)]),
                                                validators=[lambda y: y in [2023, 2022]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))
    client = django_filters.ModelChoiceFilter(queryset=Partners.objects.all(), empty_label="Все контрагенты",
                                              widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = Outgoing
        fields = ['outgoing_year', 'company', 'client']


class OrderFilter(django_filters.FilterSet):
    order_year = django_filters.NumberFilter(field_name='date__year', lookup_expr='exact',
                                             widget=forms.Select(attrs={'class': 'dropdown'},
                                                                 choices=[(2023, 2023), (2022, 2022)]),
                                             validators=[lambda y: y in [2023, 2022]])
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = Order
        fields = ['order_year', 'company']
