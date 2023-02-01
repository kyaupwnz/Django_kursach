import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from my_mail.models import Client, Message, MailingList, SendingAttempt


# Create your views here.


def hello(request):
    return render(request, 'my_mail/index.html')


def registration(request):
    return render(request, 'my_mail/registration.html')


def home(request):
    return render(request, 'my_mail/home.html')


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('my_mail:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('my_mail:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('my_mail:client_list')


class ClientDetailView(DetailView):
    model = Client


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('my_mail:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('my_mail:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('my_mail:message_list')


class MessageDetailView(DetailView):
    model = Message


class MailingListListView(ListView):
    model = MailingList


class MailingListCreateView(CreateView):
    model = MailingList
    fields = '__all__'
    success_url = reverse_lazy('my_mail:mailing_list')


class MailingListUpdateView(UpdateView):
    model = MailingList
    fields = '__all__'
    success_url = reverse_lazy('my_mail:mailing_list')


class MailingListDeleteView(DeleteView):
    model = MailingList
    fields = '__all__'
    success_url = reverse_lazy('my_mail:mailing_list')


class MailingListDetailView(DetailView):
    model = MailingList


def statistics(request):
    context = {
        'object_list': SendingAttempt.objects.all()
    }
    return render(request, 'my_mail/statistics.html', context)
