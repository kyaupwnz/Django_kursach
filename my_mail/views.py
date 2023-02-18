import datetime

from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from blog.models import Record
from my_mail.forms import MailingListForm, ClientForm, MessageForm
from my_mail.models import Client, Message, MailingList, SendingAttempt


# Create your views here.

class HomeView(TemplateView):
    template_name = 'my_mail/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog'] = Record.objects.all().order_by('?')[:3]
        context_data['count_mailing_all'] = MailingList.objects.all().count()
        context_data['count_mailing_active'] = MailingList.objects.filter(mail_status=MailingList.STARTED).count()
        context_data['count_unique_clients'] = Client.objects.all().count()
        return context_data


class ClientListView(ListView):
    model = Client

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('my_mail.view_client'):
            return queryset
        return Client.objects.filter(owner=self.request.user)


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('my_mail:client_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('my_mail:client_list')

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('my_mail:client_list')

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)


class ClientDetailView(DetailView):
    model = Client

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)


class MessageListView(ListView):
    model = Message

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('my_mail.view_message'):
            return queryset
        return Message.objects.filter(owner=self.request.user)


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('my_mail:message_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('my_mail:message_list')

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('my_mail:message_list')

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MessageDetailView(DetailView):
    model = Message

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MailingListListView(ListView):
    model = MailingList

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('my_mail.view_mailinglist'):
            return queryset
        return MailingList.objects.filter(owner=self.request.user)


class MailingListCreateView(CreateView):
    model = MailingList
    form_class = MailingListForm
    success_url = reverse_lazy('my_mail:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super().form_valid(form)


class MailingListUpdateView(UpdateView):
    model = MailingList
    fields = '__all__'
    success_url = reverse_lazy('my_mail:mailing_list')

    def get_queryset(self):
        return MailingList.objects.filter(owner=self.request.user)


class MailingListDeleteView(DeleteView):
    model = MailingList
    fields = '__all__'
    success_url = reverse_lazy('my_mail:mailing_list')

    def get_queryset(self):
        return MailingList.objects.filter(owner=self.request.user)


class MailingListDetailView(DetailView):
    model = MailingList

    def get_queryset(self):
        return MailingList.objects.filter(owner=self.request.user)


def statistics(request):
    context = {
        'object_list': SendingAttempt.objects.all()
    }
    return render(request, 'my_mail/statistics.html', context)


@permission_required('my_mail.set_mail_status')
def set_mail_status(request, pk):
    obj = get_object_or_404(MailingList, pk=pk)
    if obj:
        obj.mail_status = MailingList.COMPLETED
        obj.save()
    return redirect(request.META.get('HTTP_REFERER'))
