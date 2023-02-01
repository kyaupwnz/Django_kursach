from my_mail.models import MailingList, SendingAttempt
from datetime import datetime, timedelta

from my_mail.service import send_message


def automatic_mailing():

    for active_settings in MailingList.objects.all():
        if active_settings.mail_status == MailingList.STARTED:
            obj = SendingAttempt.objects.filter(mailing_list=active_settings).last()

            if obj is None:
                mailing_time = active_settings.mail_time.replace(second=0, microsecond=0)
                now_time = datetime.now().time().replace(second=0, microsecond=0)
                if mailing_time == now_time:
                    send_message(active_settings)

            else:
                periodicity = active_settings.periodicity
                obj_time = obj.date_time

                if periodicity == MailingList.DAILY:
                    obj_time += timedelta(days=1)
                elif periodicity == MailingList.WEEKLY:
                    obj_time += timedelta(days=7)
                elif periodicity == MailingList.MONTHLY:
                    obj_time += timedelta(days=30)
                obj_time = obj_time.replace(second=0, microsecond=0)
                now_time = datetime.now().replace(second=0, microsecond=0)
                if obj_time == now_time:
                    send_message(active_settings)
