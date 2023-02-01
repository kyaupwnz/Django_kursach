from django.conf import settings
from django.core.mail import send_mail
from my_mail.models import MailingList, SendingAttempt


def send_message(active_settings):
    status_list = []
    mail_list = active_settings.client.all()
    for item in mail_list:
        try:
            send_mail(
                subject=active_settings.message.title,
                message=active_settings.message.content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[item.email],
                fail_silently=False
            )
        except:
            server_response = {'attempt_status': 'Не доставлено',
                               'server_response': item.email,
                               'mailing_list': MailingList.objects.get(pk=active_settings.id)}
            status_list.append(SendingAttempt(**server_response))

        else:
            server_response = {'attempt_status': 'Доставлено',
                               'server_response': item.email,
                               'mailing_list': MailingList.objects.get(pk=active_settings.id)}
            status_list.append(SendingAttempt(**server_response))
    SendingAttempt.objects.bulk_create(status_list)
