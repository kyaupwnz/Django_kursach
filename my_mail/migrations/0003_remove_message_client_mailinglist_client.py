# Generated by Django 4.1.5 on 2023-01-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_mail', '0002_remove_message_client_message_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='client',
        ),
        migrations.AddField(
            model_name='mailinglist',
            name='client',
            field=models.ManyToManyField(to='my_mail.client', verbose_name='Адресат'),
        ),
    ]
