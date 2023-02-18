from django import forms

from my_mail.models import MailingList, Client, Message
from users.forms import StyleFormMixin


class MailingListForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MailingList
        fields = '__all__'
        exclude = ['owner']


class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['owner']


class MessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['owner']
