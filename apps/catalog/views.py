from datetime import datetime, date
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils import dateformat
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django_filters.views import FilterView

from apps.catalog.models import Partners, Companies, Workers
from apps.catalog.forms import PartnersForm, CompaniesForm, WorkersForm
from apps.catalog.filter import PhonebookFilter, PartnersFilter, WorkersFilter


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        form.instance.author_created = self.request.user
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class BirthdayFullRequiredMixin:
    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        return user_passes_test(lambda u: u.groups.filter(name='Birthday_Full').exists(),
                                login_url=reverse_lazy('login'))(view)


class PartnersRequiredMixin:
    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        return user_passes_test(lambda u: u.groups.filter(name='Partners').exists(),
                                login_url=reverse_lazy('login'))(view)


class CompaniesRequiredMixin:
    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        return user_passes_test(lambda u: u.groups.filter(name='Companies').exists(),
                                login_url=reverse_lazy('login'))(view)


class WorkersRequiredMixin:
    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        return user_passes_test(lambda u: u.groups.filter(name='Workers').exists(),
                                login_url=reverse_lazy('login'))(view)


class LoginUserView(LoginView):
    template_name = 'catalog/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class PhonebookListView(FilterView):
    filterset_class = PhonebookFilter
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        kwargs['workers'] = Workers.objects.all().order_by('surname')
        kwargs['filter'] = PhonebookFilter(self.request.GET, queryset=kwargs['workers'])
        return super().get_context_data(**kwargs)


class BirthdayTemplateView(TemplateView):
    template_name = 'catalog/birthday.html'

    def get_context_data(self, **kwargs):
        current_month = dateformat.format(datetime.now(), 'F')
        today = date.today()
        next_month = (today.month % 12) + 1
        russian_month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь",
                               "Октябрь", "Ноябрь", "Декабрь"]

        kwargs['current_month'] = current_month
        kwargs['next_month_name'] = russian_month_names[next_month - 1]
        kwargs['workers_this_month'] = Workers.objects.filter(birthday__month=today.month).order_by('birthday__day')
        kwargs['workers_next_month'] = Workers.objects.filter(birthday__month=next_month).order_by('birthday__day')

        for worker in kwargs['workers_this_month']:
            age = today.year - worker.birthday.year - (
                    (today.month, today.day) < (worker.birthday.month, worker.birthday.day))
            worker.age = age

        for worker in kwargs['workers_next_month']:
            age = today.year - worker.birthday.year + (
                    (next_month, worker.birthday.day) < (today.month, today.day))
            worker.age = age

        return super().get_context_data(**kwargs)


class BirthdayFullTemplateView(BirthdayFullRequiredMixin, BirthdayTemplateView):
    template_name = 'catalog/birthday_full.html'


class PartnersListView(PartnersRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = Partners
    form_class = PartnersForm
    filterset_class = PartnersFilter
    template_name = 'catalog/partners.html'
    success_url = reverse_lazy('partners')
    success_msg = 'Запись создана'

    def get(self, request, *args, **kwargs):
        if 'company' in request.GET:
            return super().get(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'company' not in request.POST:
            return super().post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['partners'] = Partners.objects.all().order_by('name')
        kwargs['filter'] = PartnersFilter(self.request.GET, queryset=kwargs['partners'])
        return super().get_context_data(**kwargs)


class PartnersUpdateView(PartnersRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Partners
    form_class = PartnersForm
    template_name = 'catalog/partners.html'
    success_url = reverse_lazy('partners')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class PartnersDeleteView(PartnersRequiredMixin, DeleteView):
    model = Partners
    template_name = 'catalog/partners.html'
    success_url = reverse_lazy('partners')
    success_msg = 'Запись удалена'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class CompaniesCreateView(CompaniesRequiredMixin, CustomSuccessMessageMixin, CreateView):
    model = Companies
    form_class = CompaniesForm
    template_name = 'catalog/companies.html'
    success_url = reverse_lazy('companies')
    success_msg = 'Запись создана'

    def get_context_data(self, **kwargs):
        kwargs['companies'] = Companies.objects.all().order_by('id')
        return super().get_context_data(**kwargs)


class CompaniesUpdateView(CompaniesRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Companies
    form_class = CompaniesForm
    template_name = 'catalog/companies.html'
    success_url = reverse_lazy('companies')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class CompaniesDeleteView(CompaniesRequiredMixin, DeleteView):
    model = Companies
    template_name = 'catalog/companies.html'
    success_url = reverse_lazy('companies')
    success_msg = 'Запись удалена'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class WorkersListView(WorkersRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = Workers
    form_class = WorkersForm
    filterset_class = WorkersFilter
    template_name = 'catalog/workers.html'
    success_url = reverse_lazy('workers')
    success_msg = 'Запись создана'

    def get(self, request, *args, **kwargs):
        if 'company' in request.GET:
            return super().get(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'company' not in request.POST:
            return super().post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        queryset = self.get_queryset().order_by('surname')
        kwargs['workers'] = queryset
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        company = self.request.GET.get('company')
        fired = self.request.GET.get('fired')
        url = reverse('workers')
        if company:
            url += f'?company={company}'
        if fired:
            url += f'&fired={fired}'
        return redirect(url)


class WorkersUpdateView(WorkersRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Workers
    form_class = WorkersForm
    template_name = 'catalog/workers.html'
    success_url = reverse_lazy('workers')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class WorkersDeleteView(WorkersRequiredMixin, DeleteView):
    model = Workers
    template_name = 'catalog/workers.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('workers')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request, *args, **kwargs)
