from datetime import date

from django.conf import settings
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(max_length=50, verbose_name='Электронный почтовый адрес')
    full_name = models.CharField(max_length=100, verbose_name='Фио', **NULLABLE)
    comment = models.TextField(max_length=250, verbose_name='Комментарий', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE,
                              **NULLABLE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тема письма')
    content = models.CharField(max_length=500, verbose_name='Тело письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE,
                              **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailingList(models.Model):
    DAILY = "Ежедневно"
    WEEKLY = "Еженедельно"
    MONTHLY = "Ежемесячно"

    PERIODICITY_CHOICES = [
        (DAILY, "Ежедневно"),
        (WEEKLY, "Еженедельно"),
        (MONTHLY, "Ежемесячно")
    ]

    COMPLETED = 'Завершена'
    CREATED = 'Создана'
    STARTED = 'Запущена'

    STATUS_CHOICES = [
        (COMPLETED, 'Завершена'),
        (CREATED, 'Создана'),
        (STARTED, 'Запущена')
    ]

    mail_time = models.TimeField(verbose_name='Время рассылки', **NULLABLE)
    periodicity = models.CharField(choices=PERIODICITY_CHOICES, max_length=50, verbose_name='Периодичность', **NULLABLE)
    mail_status = models.CharField(choices=STATUS_CHOICES, max_length=10, default=CREATED, verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, verbose_name='Сообщение', on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today, verbose_name='Начальная дата')
    end_date = models.DateField(default=date.today, verbose_name='Конечная дата')
    client = models.ManyToManyField(Client, verbose_name='Адресат')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'Время {self.mail_time}, периодичность {self.periodicity}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        permissions = [
            ('set_mail_status', 'Can set mailing status'),
        ]


class SendingAttempt(models.Model):
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки', **NULLABLE)
    attempt_status = models.CharField(max_length=250, verbose_name='Статус попытки', **NULLABLE)
    server_response = models.CharField(max_length=250, verbose_name='Ответ сервера', **NULLABLE)
    mailing_list = models.ForeignKey(MailingList, null=True, verbose_name='Список Рассылки', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date_time} {self.attempt_status} {self.server_response} '

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'


