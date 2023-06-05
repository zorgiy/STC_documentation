from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from apps.catalog.forms import PartnersForm
from apps.catalog.views import CustomSuccessMessageMixin
from apps.catalog.models import Partners, Workers
from apps.reception.models import Incoming, Outgoing, Order
from apps.reception.filter import IncomingFilter, OutgoingFilter, OrderFilter
from apps.reception.forms import IncomingForm, OutgoingForm, OrderForm


class ReceptionRequiredMixin:
    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        return user_passes_test(lambda u: u.groups.filter(name='Reception').exists(),
                                login_url=reverse_lazy('login'))(view)


class IncDocListView(ReceptionRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = Incoming
    form_class = IncomingForm
    filterset_class = IncomingFilter
    template_name = 'reception/inc_doc.html'
    success_url = reverse_lazy('inc_doc')
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
        kwargs['inc_doc'] = Incoming.objects.all().order_by('-receipt_date')
        kwargs['partners_form'] = PartnersForm()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        incoming_year = self.request.GET.get('incoming_year')
        company = self.request.GET.get('company')
        client = self.request.GET.get('client')
        url = reverse('inc_doc')
        if incoming_year:
            url += f'?incoming_year={incoming_year}'
        if company:
            url += f'&company={company}'
        if client:
            url += f'&client={client}'
        return redirect(url)


class IncDocUpdateView(ReceptionRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Incoming
    form_class = IncomingForm
    template_name = 'reception/inc_doc.html'
    success_url = reverse_lazy('inc_doc')
    success_msg = 'Запись обновлена'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['client'].queryset = Partners.objects.all().order_by('name')
        return form

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class IncDocDeleteView(ReceptionRequiredMixin, DeleteView):
    model = Incoming
    template_name = 'reception/inc_doc.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('inc_doc')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class OutDocListView(ReceptionRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = Outgoing
    form_class = OutgoingForm
    filterset_class = OutgoingFilter
    template_name = 'reception/out_doc.html'
    success_url = reverse_lazy('out_doc')
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
        kwargs['out_doc'] = Outgoing.objects.all().order_by('-receipt_date')
        kwargs['partners_form'] = PartnersForm()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        outgoing_year = self.request.GET.get('outgoing_year')
        company = self.request.GET.get('company')
        client = self.request.GET.get('client')
        url = reverse('out_doc')
        if outgoing_year:
            url += f'?outgoing_year={outgoing_year}'
        if company:
            url += f'&company={company}'
        if client:
            url += f'&client={client}'
        return redirect(url)


class OutDocUpdateView(ReceptionRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Outgoing
    form_class = OutgoingForm
    template_name = 'reception/out_doc.html'
    success_url = reverse_lazy('out_doc')
    success_msg = 'Запись обновлена'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['client'].queryset = Partners.objects.all().order_by('name')
        return form

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class OutDocDeleteView(ReceptionRequiredMixin, DeleteView):
    model = Outgoing
    template_name = 'reception/out_doc.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('out_doc')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class OrderListView(ReceptionRequiredMixin, CustomSuccessMessageMixin, CreateView, FilterView):
    model = Order
    form_class = OrderForm
    filterset_class = OrderFilter
    template_name = 'reception/order.html'
    success_url = reverse_lazy('order')
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
        kwargs['order'] = Order.objects.all().order_by('-date')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        order_year = self.request.GET.get('order_year')
        company = self.request.GET.get('company')
        url = reverse('order')
        if order_year:
            url += f'?order_year={order_year}'
        if company:
            url += f'&company={company}'
        return redirect(url)


class OrderUpdateView(ReceptionRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'reception/order.html'
    success_url = reverse_lazy('order')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class OrderDeleteView(ReceptionRequiredMixin, DeleteView):
    model = Order
    template_name = 'reception/order.html'
    success_msg = 'Запись удалена'

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        return referer or reverse_lazy('order')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class ReceiptListView(ReceptionRequiredMixin, ListView):
    model = Workers
    template_name = 'reception/receipt.html'
