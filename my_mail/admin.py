from django.contrib import admin

from my_mail.models import Client, Message, MailingList, SendingAttempt


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'comment',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', )
    list_filter = ('title',)


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('mail_time', 'periodicity', 'mail_status', 'message',)
    list_filter = ('periodicity', 'mail_status', 'message',)


@admin.register(SendingAttempt)
class SendingAttemptAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'attempt_status', 'server_response', 'mailing_list',)
    list_filter = ('attempt_status', 'server_response', )
