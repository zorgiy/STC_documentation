from datetime import date

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField


class Partners(models.Model):
    name = models.CharField('Название', max_length=100)
    city = models.CharField('Город', max_length=40, blank=True)
    telephone = PhoneNumberField('Телефон', blank=True)
    email = models.EmailField(max_length=80, blank=True)
    general_director = models.CharField('Генеральный директор', max_length=100, blank=True)
    the_contact_person = models.CharField('Контактное лицо', max_length=100, blank=True)
    mailing_address = models.CharField('Почтовый адрес', max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
        ordering = ('id',)


class Companies(models.Model):
    name = models.CharField('Название', max_length=100)
    index = models.CharField('Индекс', max_length=15)
    telephone = PhoneNumberField('Телефон', blank=True)
    mailing_address = models.CharField('Почтовый адрес', max_length=150, blank=True)
    last_document_number_incoming = models.PositiveIntegerField('Номер последнего входящего документа', default=0,
                                                                blank=True)
    last_document_number_outgoing = models.PositiveIntegerField('Номер последнего исходящего документа', default=0,
                                                                blank=True)
    last_document_number_order = models.PositiveIntegerField('Номер последнего приказа', default=0, blank=True)
    last_document_year = models.PositiveIntegerField('Год последнего документа', default=timezone.now().year,
                                                     blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ('id',)


class Workers(models.Model):
    FIRED_TYPES = [
        ('нет', 'Нет'),
        ('да', 'Да')
    ]
    company = models.ForeignKey(Companies, on_delete=models.PROTECT, verbose_name='Компания')
    surname = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Отчество', max_length=50, blank=True)
    birthday = models.DateField('Дата рождения', null=True, blank=True)
    position = models.CharField('Должность', max_length=180, blank=True)
    telephone = PhoneNumberField('Телефон', blank=True)
    internal_telephone = models.CharField('Внутренний телефон', max_length=4, default='', blank=True,
                                          validators=[RegexValidator(r'^\d{4}$', 'Введите 4 цифры')])
    cellular = PhoneNumberField('Сотовый телефон', blank=True)
    email = models.EmailField(max_length=80, blank=True)
    fired = models.CharField('Уволен', choices=FIRED_TYPES, max_length=3, default='нет')

    def is_birthday_today(self):
        today = date.today()
        return (
            self.birthday.day == today.day and
            self.birthday.month == today.month
        )

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ('surname',)
