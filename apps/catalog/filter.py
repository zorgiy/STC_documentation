import django_filters
from django import forms
from django.db.models import Q

from apps.catalog.models import Partners, Companies, Workers


class PhonebookFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='search', label='Поиск',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    @staticmethod
    def search(queryset, name, value):
        return queryset.filter(
            Q(surname__icontains=value) |
            Q(first_name__icontains=value) |
            Q(second_name__icontains=value) |
            Q(cellular__exact=value) |
            Q(telephone__exact=value) |
            Q(internal_telephone__exact=value) |
            Q(email__icontains=value) |
            Q(position__icontains=value)
        )

    class Meta:
        model = Workers
        fields = []


class PartnersFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='search', label='Поиск',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    @staticmethod
    def search(queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(city__icontains=value) |
            Q(telephone__exact=value) |
            Q(email__icontains=value) |
            Q(general_director__icontains=value) |
            Q(the_contact_person__icontains=value) |
            Q(mailing_address__icontains=value)
        )

    class Meta:
        model = Partners
        fields = []


class WorkersFilter(django_filters.FilterSet):
    FIRED_CHOICES = [
        ('нет', 'Работающие'),
        ('да', 'Уволенные')
    ]
    company = django_filters.ModelChoiceFilter(queryset=Companies.objects.all(), empty_label="Все компании",
                                               widget=forms.Select(attrs={'class': 'dropdown'}))
    fired = django_filters.ChoiceFilter(choices=FIRED_CHOICES, empty_label="Все сотрудники", initial='нет',
                                        widget=forms.Select(attrs={'class': 'dropdown'}))

    class Meta:
        model = Workers
        fields = ['company', 'fired']
