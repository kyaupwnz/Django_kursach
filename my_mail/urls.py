from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.decorators.cache import cache_page

from my_mail.apps import MyMailConfig
from my_mail.views import ClientCreateView, ClientListView, ClientUpdateView, \
    ClientDeleteView, MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingListListView, \
    MailingListCreateView, MailingListUpdateView, MailingListDeleteView, ClientDetailView, MessageDetailView, \
    MailingListDetailView, statistics, set_mail_status, HomeView

app_name = MyMailConfig.name

urlpatterns = [
    path('', cache_page(60)(HomeView.as_view()), name='home'),
    path('home/', cache_page(60)(HomeView.as_view()), name='home'),
    path('client_list/', login_required(ClientListView.as_view()), name='client_list'),
    path('create_client/', login_required(ClientCreateView.as_view()), name='create_client'),
    path('update_client/<int:pk>/', login_required(ClientUpdateView.as_view()), name='update_client'),
    path('delete_client/<int:pk>/', login_required(ClientDeleteView.as_view()), name='delete_client'),
    path('detail_client/<int:pk>/', login_required(ClientDetailView.as_view()), name='detail_client'),
    path('message_list/', login_required(MessageListView.as_view()), name='message_list'),
    path('create_message/', login_required(MessageCreateView.as_view()), name='create_message'),
    path('update_message/<int:pk>/', login_required(MessageUpdateView.as_view()), name='update_message'),
    path('delete_message/<int:pk>/', login_required(MessageDeleteView.as_view()), name='delete_message'),
    path('detail_message/<int:pk>/', login_required(MessageDetailView.as_view()), name='detail_message'),
    path('mailing_list/', login_required(MailingListListView.as_view()), name='mailing_list'),
    path('create_mailing_list/', login_required(MailingListCreateView.as_view()), name='create_mailing_list'),
    path('update_mailing_list/<int:pk>/', login_required(MailingListUpdateView.as_view()), name='update_mailing_list'),
    path('delete_mailing_list/<int:pk>/', login_required(MailingListDeleteView.as_view()), name='delete_mailing_list'),
    path('detail_mailing_list/<int:pk>/', login_required(MailingListDetailView.as_view()), name='detail_mailing_list'),
    path('statistics/', login_required(statistics), name='statistics'),
    path('set_mail_status/<int:pk>', login_required(set_mail_status), name='set_mail_status')
]
