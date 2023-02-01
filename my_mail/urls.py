from django.urls import path
from my_mail.apps import MyMailConfig
from my_mail.views import hello, registration, home, ClientCreateView, ClientListView, ClientUpdateView, \
    ClientDeleteView, MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingListListView, \
    MailingListCreateView, MailingListUpdateView, MailingListDeleteView, ClientDetailView, MessageDetailView, \
    MailingListDetailView,  statistics

app_name = MyMailConfig.name

urlpatterns = [
    path('', hello),
    path('registration/', registration, name='registration'),
    path('home/', home, name='home'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('detail_client/<int:pk>/', ClientDetailView.as_view(), name='detail_client'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('update_message/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),
    path('detail_message/<int:pk>/', MessageDetailView.as_view(), name='detail_message'),
    path('mailing_list/', MailingListListView.as_view(), name='mailing_list'),
    path('create_mailing_list/', MailingListCreateView.as_view(), name='create_mailing_list'),
    path('update_mailing_list/<int:pk>/', MailingListUpdateView.as_view(), name='update_mailing_list'),
    path('delete_mailing_list/<int:pk>/', MailingListDeleteView.as_view(), name='delete_mailing_list'),
    path('detail_mailing_list/<int:pk>/', MailingListDetailView.as_view(), name='detail_mailing_list'),
    path('statistics/', statistics, name='statistics'),
]
