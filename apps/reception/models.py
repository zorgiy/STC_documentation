from django.db import models
from django.contrib.auth.models import User
from apps.catalog.models import Companies, Partners, Workers


class Incoming(models.Model):
    RECEIPT_TYPES = (
        ('Лично', 'Лично'),
        ('Электронная почта', 'Электронная почта'),
        ('Почта России', 'Почта России')
    )
    EXECUTION_TYPES = (
        ('Лесникова Е.И.', 'Лесникова Е.И.'),
        ('Князев Ю.И.', 'Князев Ю.И.'),
        ('Юрак М.В.', 'Юрак М.В.')
    )
    company = models.ForeignKey(Companies, related_name='company_incoming', on_delete=models.PROTECT,
                                verbose_name='Компания', default=1)
    index = models.CharField('Индекс', max_length=16)
    receipt_date = models.DateField('Дата поступления')
    document_number = models.CharField('№ документа', max_length=20, blank=True)
    document_date = models.DateField('Дата документа')
    client = models.ForeignKey(Partners, on_delete=models.PROTECT, verbose_name='Контрагент')
    summary = models.TextField('Краткое содержание')
    author = models.ForeignKey(Workers, related_name='author_incoming', on_delete=models.PROTECT,
                               verbose_name='Исполнитель')
    type_of_receipt = models.CharField('Вид получения', choices=RECEIPT_TYPES, max_length=20, default='Лично')
    execution_control = models.CharField('Контроль об исполнении', choices=EXECUTION_TYPES,
                                         max_length=15, default='Лесникова Е.И.')
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.index}: {self.client} ({self.summary}) исполнитель: {self.author} /автор: {self.author_created}/'

    class Meta:
        verbose_name = 'Входящий документ'
        verbose_name_plural = 'Входящие документы'
        ordering = ('-id',)


class Outgoing(models.Model):
    RECEIPT_TYPES = (
        ('Лично', 'Лично'),
        ('Электронная почта', 'Электронная почта'),
        ('Почта России', 'Почта России'),
        ('Экспресс-почта', 'Экспресс-почта')
    )
    EXECUTION_TYPES = (
        ('Лесникова Е.И.', 'Лесникова Е.И.'),
        ('Князев Ю.И.', 'Князев Ю.И.'),
        ('Юрак М.В.', 'Юрак М.В.'),
        ('Рубин С.Ю.', 'Рубин С.Ю.'),
        ('Иванова Т.Л.', 'Иванова Т.Л.')
    )
    company = models.ForeignKey(Companies, related_name='company_outgoing', on_delete=models.PROTECT,
                                verbose_name='Компания', default=1)
    index = models.CharField('Индекс', max_length=16)
    receipt_date = models.DateField('Дата поступления')
    client = models.ForeignKey(Partners, on_delete=models.PROTECT, verbose_name='Контрагент')
    summary = models.TextField('Краткое содержание')
    signed = models.ForeignKey(Workers, related_name='signed_outgoing', on_delete=models.PROTECT,
                               verbose_name='Документ подписал')
    author = models.ForeignKey(Workers, related_name='author_outgoing', on_delete=models.PROTECT,
                               verbose_name='Исполнитель')
    type_of_receipt = models.CharField('Вид отправки', choices=RECEIPT_TYPES,
                                       max_length=20, default='Электронная почта')
    execution_control = models.CharField('Контроль об исполнении', choices=EXECUTION_TYPES,
                                         max_length=15, default='Лесникова Е.И.')
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.index}: {self.client} ({self.summary}) исполнитель: {self.signed} /автор: {self.author_created}/'

    class Meta:
        verbose_name = 'Исходящий документ'
        verbose_name_plural = 'Исходящие документы'
        ordering = ('-id',)


class Order(models.Model):
    ADDITIONAL_TYPES = (
        ('по списку', 'по списку'),
    )
    EXECUTION_TYPES = (
        ('Лесникова Е.И.', 'Лесникова Е.И.'),
        ('Князев Ю.И.', 'Князев Ю.И.'),
        ('Юрак М.В.', 'Юрак М.В.')
    )
    company = models.ForeignKey(Companies, related_name='company_order', on_delete=models.PROTECT,
                                verbose_name='Компания', default=1)
    number = models.CharField('Номер', max_length=10)
    date = models.DateField('Дата')
    summary = models.TextField('Краткое содержание')
    author = models.ForeignKey(Workers, related_name='author_order', on_delete=models.PROTECT,
                               verbose_name='Исполнитель')
    additional_authors = models.CharField('Дополнительные исполнители', choices=ADDITIONAL_TYPES,
                                          max_length=10, default='по списку')
    period_of_execution = models.DateField('Срок исполнения')
    execution_control = models.CharField('Контроль об исполнении', choices=EXECUTION_TYPES,
                                         max_length=15, default='Лесникова Е.И.')
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.number}: {self.summary}, исполнитель: {self.author} /автор: {self.author_created}/'

    class Meta:
        verbose_name = 'Приказ'
        verbose_name_plural = 'Приказы'
        ordering = ('-id',)
