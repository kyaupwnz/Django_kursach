from django.core.management import BaseCommand

from my_mail.mailsender import automatic_mailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        automatic_mailing()
