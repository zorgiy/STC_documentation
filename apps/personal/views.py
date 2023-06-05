from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from apps.catalog.views import CustomSuccessMessageMixin
from apps.personal.filter import LogActsFilter, LogContractFilter, LogAddAgreementsFilter, LogOrdersKFilter, \
    LogOrdersLSFilter, LogOrdersShFilter, LogWorkContractsFilter, RegisterFinSupportFilter
from apps.personal.forms import LogActsForm, LogContractForm, LogAddAgreementsForm, LogOrdersKForm, LogOrdersLSForm, \
    LogOrdersShForm, LogWorkContractsForm, RegisterFinSupportForm
from apps.personal.models import LogActs, LogContract, LogAddAgreements, LogOrdersK, LogOrdersLS, LogOrdersSh, \
    LogWorkContracts, RegisterFinSupport


class PersonalRequiredMixin:
    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        return user_passes_test(lambda u: u.groups.filter(name='Personal').exists(),
                                login_url=reverse_lazy('login'))(view)


class LogActsListView(PersonalRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = LogActs
    form_class = LogActsForm
    filterset_class = LogActsFilter
    template_name = 'personal/log_acts.html'
    success_url = reverse_lazy('log_acts')
    success_msg = 'Запись создана'

    def get(self, request, *args, **kwargs):
        if 'company' in request.GET:
            return super().get(request, *args, **kwargs)
        return super(CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'company' not in request.POST:
            return super(CreateView, self).post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['log_acts'] = LogActs.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        log_acts_year = self.request.GET.get('log_acts_year')
        company = self.request.GET.get('company')
        url = reverse('log_acts')
        if log_acts_year:
            url += f'?log_acts_year={log_acts_year}'
        if company:
            url += f'&company={company}'
        return redirect(url)


class LogActsUpdateView(PersonalRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = LogActs
    form_class = LogActsForm
    template_name = 'personal/log_acts.html'
    success_url = reverse_lazy('log_acts')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class LogActsDeleteView(PersonalRequiredMixin, DeleteView):
    model = LogActs
    template_name = 'personal/log_acts.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('log_acts')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class LogContractListView(PersonalRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = LogContract
    form_class = LogContractForm
    filterset_class = LogContractFilter
    template_name = 'personal/log_contract.html'
    success_url = reverse_lazy('log_contract')
    success_msg = 'Запись создана'

    def get(self, request, *args, **kwargs):
        if 'company' in request.GET:
            return super().get(request, *args, **kwargs)
        return super(CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'company' not in request.POST:
            return super(CreateView, self).post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['log_contract'] = LogContract.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        log_contract_year = self.request.GET.get('log_contract_year')
        company = self.request.GET.get('company')
        url = reverse('log_contract')
        if log_contract_year:
            url += f'?log_contract_year={log_contract_year}'
        if company:
            url += f'&company={company}'
        return redirect(url)


class LogContractUpdateView(PersonalRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = LogContract
    form_class = LogContractForm
    template_name = 'personal/log_contract.html'
    success_url = reverse_lazy('log_contract')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class LogContractDeleteView(PersonalRequiredMixin, DeleteView):
    model = LogContract
    template_name = 'personal/log_contract.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('log_contract')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class LogAddAgreementsListView(PersonalRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = LogAddAgreements
    form_class = LogAddAgreementsForm
    filterset_class = LogAddAgreementsFilter
    template_name = 'personal/log_add_agreements.html'
    success_url = reverse_lazy('log_add_agreements')
    success_msg = 'Запись создана'

    def get(self, request, *args, **kwargs):
        if 'company' in request.GET:
            return super().get(request, *args, **kwargs)
        return super(CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'company' not in request.POST:
            return super(CreateView, self).post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['log_add_agreements'] = LogAddAgreements.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        log_add_agreements_year = self.request.GET.get('log_add_agreements_year')
        company = self.request.GET.get('company')
        url = reverse('log_add_agreements')
        if log_add_agreements_year:
            url += f'?log_add_agreements_year={log_add_agreements_year}'
        if company:
            url += f'&company={company}'
        return redirect(url)


class LogAddAgreementsUpdateView(PersonalRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = LogAddAgreements
    form_class = LogAddAgreementsForm
    template_name = 'personal/log_add_agreements.html'
    success_url = reverse_lazy('log_add_agreements')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class LogAddAgreementsDeleteView(PersonalRequiredMixin, DeleteView):
    model = LogAddAgreements
    template_name = 'personal/log_add_agreements.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('log_add_agreements')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class LogOrdersKListView(PersonalRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = LogOrdersK
    form_class = LogOrdersKForm
    filterset_class = LogOrdersKFilter
    template_name = 'personal/log_orders_K.html'
    success_url = reverse_lazy('log_orders_K')
    success_msg = 'Запись создана'

    def get(self, request, *args, **kwargs):
        if 'company' in request.GET:
            return super().get(request, *args, **kwargs)
        return super(CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'company' not in request.POST:
            return super(CreateView, self).post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['log_orders_K'] = LogOrdersK.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        log_orders_k_year = self.request.GET.get('log_orders_K_year')
        company = self.request.GET.get('company')
        worker = self.request.GET.get('worker')
        reason = self.request.GET.get('reason')
        url = reverse('log_orders_K')
        if log_orders_k_year:
            url += f'?log_orders_K_year={log_orders_k_year}'
        if company:
            url += f'&company={company}'
        if worker:
            url += f'&worker={worker}'
        if reason:
            url += f'&reason={reason}'
        return redirect(url)


class LogOrdersKUpdateView(PersonalRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = LogOrdersK
    form_class = LogOrdersKForm
    template_name = 'personal/log_orders_K.html'
    success_url = reverse_lazy('log_orders_K')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class LogOrdersKDeleteView(PersonalRequiredMixin, DeleteView):
    model = LogOrdersK
    template_name = 'personal/log_orders_K.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('log_orders_K')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class LogOrdersLSListView(PersonalRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = LogOrdersLS
    form_class = LogOrdersLSForm
    filterset_class = LogOrdersLSFilter
    template_name = 'personal/log_orders_LS.html'
    success_url = reverse_lazy('log_orders_LS')
    success_msg = 'Запись создана'

    def get(self, request, *args, **kwargs):
        if 'company' in request.GET:
            return super().get(request, *args, **kwargs)
        return super(CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'company' not in request.POST:
            return super(CreateView, self).post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['log_orders_LS'] = LogOrdersLS.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        log_orders_ls_year = self.request.GET.get('log_orders_LS_year')
        company = self.request.GET.get('company')
        worker = self.request.GET.get('worker')
        reason = self.request.GET.get('reason')
        url = reverse('log_orders_LS')
        if log_orders_ls_year:
            url += f'?log_orders_LS_year={log_orders_ls_year}'
        if company:
            url += f'&company={company}'
        if worker:
            url += f'&worker={worker}'
        if reason:
            url += f'&reason={reason}'
        return redirect(url)


class LogOrdersLSUpdateView(PersonalRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = LogOrdersLS
    form_class = LogOrdersLSForm
    template_name = 'personal/log_orders_LS.html'
    success_url = reverse_lazy('log_orders_LS')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class LogOrdersLSDeleteView(PersonalRequiredMixin, DeleteView):
    model = LogOrdersLS
    template_name = 'personal/log_orders_LS.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('log_orders_LS')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class LogOrdersShListView(PersonalRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = LogOrdersSh
    form_class = LogOrdersShForm
    filterset_class = LogOrdersShFilter
    template_name = 'personal/log_orders_Sh.html'
    success_url = reverse_lazy('log_orders_Sh')
    success_msg = 'Запись создана'

    def get(self, request, *args, **kwargs):
        if 'company' in request.GET:
            return super().get(request, *args, **kwargs)
        return super(CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'company' not in request.POST:
            return super(CreateView, self).post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['log_orders_Sh'] = LogOrdersSh.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        log_orders_sh_year = self.request.GET.get('log_orders_Sh_year')
        company = self.request.GET.get('company')
        url = reverse('log_orders_Sh')
        if log_orders_sh_year:
            url += f'?log_orders_Sh_year={log_orders_sh_year}'
        if company:
            url += f'&company={company}'
        return redirect(url)


class LogOrdersShUpdateView(PersonalRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = LogOrdersSh
    form_class = LogOrdersShForm
    template_name = 'personal/log_orders_Sh.html'
    success_url = reverse_lazy('log_orders_Sh')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class LogOrdersShDeleteView(PersonalRequiredMixin, DeleteView):
    model = LogOrdersSh
    template_name = 'personal/log_orders_Sh.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('log_orders_Sh')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class LogWorkContractsListView(PersonalRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = LogWorkContracts
    form_class = LogWorkContractsForm
    filterset_class = LogWorkContractsFilter
    template_name = 'personal/log_work_contracts.html'
    success_url = reverse_lazy('log_work_contracts')
    success_msg = 'Запись создана'

    def get(self, request, *args, **kwargs):
        if 'company' in request.GET:
            return super().get(request, *args, **kwargs)
        return super(CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'company' not in request.POST:
            return super(CreateView, self).post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['log_work_contracts'] = LogWorkContracts.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        log_work_contracts_year = self.request.GET.get('log_work_contracts_year')
        company = self.request.GET.get('company')
        url = reverse('log_work_contracts')
        if log_work_contracts_year:
            url += f'?log_work_contracts_year={log_work_contracts_year}'
        if company:
            url += f'&company={company}'
        return redirect(url)


class LogWorkContractsUpdateView(PersonalRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = LogWorkContracts
    form_class = LogWorkContractsForm
    template_name = 'personal/log_work_contracts.html'
    success_url = reverse_lazy('log_work_contracts')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class LogWorkContractsDeleteView(PersonalRequiredMixin, DeleteView):
    model = LogWorkContracts
    template_name = 'personal/log_work_contracts.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('log_work_contracts')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class RegisterFinSupportListView(PersonalRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = RegisterFinSupport
    form_class = RegisterFinSupportForm
    filterset_class = RegisterFinSupportFilter
    template_name = 'personal/register_fin_support.html'
    success_url = reverse_lazy('register_fin_support')
    success_msg = 'Запись создана'

    def get(self, request, *args, **kwargs):
        if 'company' in request.GET:
            return super().get(request, *args, **kwargs)
        return super(CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'company' not in request.POST:
            return super(CreateView, self).post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['register_fin_support'] = RegisterFinSupport.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        register_fin_support_year = self.request.GET.get('register_fin_support_year')
        company = self.request.GET.get('company')
        worker = self.request.GET.get('worker')
        month_of_issue = self.request.GET.get('month_of_issue')
        url = reverse('register_fin_support')
        if register_fin_support_year:
            url += f'?register_fin_support_year={register_fin_support_year}'
        if company:
            url += f'&company={company}'
        if worker:
            url += f'&worker={worker}'
        if month_of_issue:
            url += f'&month_of_issue={month_of_issue}'
        return redirect(url)


class RegisterFinSupportUpdateView(PersonalRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = RegisterFinSupport
    form_class = RegisterFinSupportForm
    template_name = 'personal/register_fin_support.html'
    success_url = reverse_lazy('register_fin_support')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class RegisterFinSupportDeleteView(PersonalRequiredMixin, DeleteView):
    model = RegisterFinSupport
    template_name = 'personal/register_fin_support.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('register_fin_support')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)
