import datetime

from django.db import models
from django.contrib.auth.models import User

from apps.catalog.models import Companies, Workers


class LogActs(models.Model):
    COMPILER_TYPES = (
        ('Бердникова О.А.', 'Бердникова О.А.'),
        ('Коростина Д.П.', 'Коростина Д.П.')
    )
    STATUS_TYPES = (
        ('нет приказа', 'нет приказа'),
        ('номер занят', 'номер занят'),
        ('подшит', 'подшит')
    )
    company = models.ForeignKey(Companies, related_name='company_log_acts', on_delete=models.PROTECT,
                                verbose_name='Компания', default=2)
    act_number = models.CharField('№ акта', max_length=20)
    date = models.DateField('Дата', default=datetime.date.today)
    worker = models.ForeignKey(Workers, related_name='worker_log_acts', on_delete=models.PROTECT,
                               verbose_name='Сотрудник')
    cause = models.TextField('Причина составления акта')
    compiler = models.CharField('Составитель', choices=COMPILER_TYPES, max_length=30, default='Коростина Д.П.')
    period = models.TextField('Период')
    execution_mark = models.CharField('Отметка об исполнении', max_length=50, blank=True)
    result = models.CharField('Результат', max_length=50, blank=True)
    status = models.CharField('Статус', choices=STATUS_TYPES, max_length=30, default='нет приказа')
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.act_number}: {self.worker} ({self.cause}) автор: {self.author_created}'

    class Meta:
        verbose_name = 'Журнал регистрации актов'
        verbose_name_plural = 'Журналы регистрации актов'
        ordering = ('-date',)


class LogContract(models.Model):
    STATUS_TYPES = (
        ('нет приказа', 'нет приказа'),
        ('номер занят', 'номер занят'),
        ('подшит', 'подшит')
    )
    company = models.ForeignKey(Companies, related_name='company_log_contract', on_delete=models.PROTECT,
                                verbose_name='Компания, с которой заключен договор', default=2)
    number = models.CharField('№', max_length=20)
    date = models.DateField('Дата', default=datetime.date.today)
    worker = models.ForeignKey(Workers, related_name='worker_log_contract', on_delete=models.PROTECT,
                               verbose_name='Сотрудник')
    content = models.TextField('Содержание')
    act_number = models.CharField('№ акта', max_length=20)
    act_date = models.DateField('Дата акта')
    status = models.CharField('Статус', choices=STATUS_TYPES, max_length=30, default='нет приказа')
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.number}: {self.worker} ({self.content}) автор: {self.author_created}'

    class Meta:
        verbose_name = 'Журнал регистрации договора Подряда'
        verbose_name_plural = 'Журналы регистрации договоров Подряда'
        ordering = ('-date',)


class LogAddAgreements(models.Model):
    STATUS_TYPES = (
        ('нет приказа', 'нет приказа'),
        ('номер занят', 'номер занят'),
        ('подшит', 'подшит')
    )
    company = models.ForeignKey(Companies, related_name='company_log_add_agreements', on_delete=models.PROTECT,
                                verbose_name='Компания', default=2)
    number = models.CharField('№', max_length=20)
    date = models.DateField('Дата', default=datetime.date.today)
    worker = models.ForeignKey(Workers, related_name='worker_log_add_agreements', on_delete=models.PROTECT,
                               verbose_name='Сотрудник')
    content = models.TextField('Содержание')
    contract_number = models.CharField('№ трудового договора', max_length=20)
    contract_date = models.DateField('Дата трудового договора')
    status = models.CharField('Статус', choices=STATUS_TYPES, max_length=30, default='нет приказа')
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.number}: {self.worker} ({self.content}) автор: {self.author_created}'

    class Meta:
        verbose_name = 'Журнал регистрации дополнительных соглашений'
        verbose_name_plural = 'Журналы регистрации дополнительных соглашений'
        ordering = ('-number',)


class LogOrdersK(models.Model):
    REASON_TYPES = (
        (' ', ' '),
        ('отпуск без сохранении ЗП', 'отпуск без сохранении ЗП'),
        ('ежегодный отпуск', 'ежегодный отпуск'),
        ('работа в выходные дни', 'работа в выходные дни'),
        ('командировка', 'командировка')
    )
    STATUS_TYPES = (
        ('нет приказа', 'нет приказа'),
        ('номер занят', 'номер занят'),
        ('подшит', 'подшит')
    )
    company = models.ForeignKey(Companies, related_name='company_log_orders_K', on_delete=models.PROTECT,
                                verbose_name='Компания', default=2)
    number = models.CharField('№', max_length=20)
    date = models.DateField('Дата', default=datetime.date.today)
    worker = models.ForeignKey(Workers, related_name='worker_log_orders_K', on_delete=models.PROTECT,
                               verbose_name='Сотрудник')
    reason = models.CharField('Причина', choices=REASON_TYPES, max_length=50, default=' ')
    description = models.TextField('Описание', blank=True)
    period = models.TextField('Период')
    status = models.CharField('Статус', choices=STATUS_TYPES, max_length=30, default='нет приказа')
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.number}: {self.worker} ({self.reason}) автор: {self.author_created}'

    class Meta:
        verbose_name = 'Журнал регистрации приказов - К'
        verbose_name_plural = 'Журналы регистрации приказов - К'
        ordering = ('-number',)


class LogOrdersLS(models.Model):
    REASON_TYPES = (
        (' ', ' '),
        ('дисциплинарное взыскание', 'дисциплинарное взыскание'),
        ('изменение  графика работы', 'изменение  графика работы'),
        ('изменение оклада', 'изменение оклада'),
        ('мат помощь к отпуску', 'мат помощь к отпуску'),
        ('мат помощь юбилей', 'мат помощь юбилей'),
        ('отмена дополнительной оплаты', 'отмена дополнительной оплаты'),
        ('перевод', 'перевод'),
        ('премия', 'премия'),
        ('приём на работу', 'приём на работу'),
        ('расторжение трудового договора', 'расторжение трудового договора'),
        ('расширение зон обслуживания', 'расширение зон обслуживания'),
        ('совмещение', 'совмещение'),
    )
    STATUS_TYPES = (
        ('нет приказа', 'нет приказа'),
        ('номер занят', 'номер занят'),
        ('подшит', 'подшит')
    )
    company = models.ForeignKey(Companies, related_name='company_log_orders_LS', on_delete=models.PROTECT,
                                verbose_name='Компания', default=2)
    number = models.CharField('№', max_length=20)
    date = models.DateField('Дата', default=datetime.date.today)
    worker = models.ForeignKey(Workers, related_name='worker_log_orders_LS', on_delete=models.PROTECT,
                               verbose_name='Сотрудник')
    reason = models.CharField('Причина', choices=REASON_TYPES, max_length=50, default=' ')
    description = models.TextField('Описание', blank=True)
    period = models.TextField('Период', blank=True)
    status = models.CharField('Статус', choices=STATUS_TYPES, max_length=30, default='нет приказа')
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.number}: {self.worker} ({self.reason}) автор: {self.author_created}'

    class Meta:
        verbose_name = 'Журнал регистрации приказов - ЛС'
        verbose_name_plural = 'Журналы регистрации приказов - ЛС'
        ordering = ('-number',)


class LogOrdersSh(models.Model):
    STATUS_TYPES = (
        ('нет приказа', 'нет приказа'),
        ('номер занят', 'номер занят'),
        ('подшит', 'подшит')
    )
    company = models.ForeignKey(Companies, related_name='company_log_orders_Sh', on_delete=models.PROTECT,
                                verbose_name='Компания', default=2)
    number = models.CharField('№', max_length=20)
    date = models.DateField('Дата', default=datetime.date.today)
    content = models.TextField('Содержание')
    period = models.TextField('Период')
    status = models.CharField('Статус', choices=STATUS_TYPES, max_length=30, default='нет приказа')
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.number} ({self.content}) автор: {self.author_created}'

    class Meta:
        verbose_name = 'Журнал регистрации приказов - Ш'
        verbose_name_plural = 'Журналы регистрации приказов - Ш'
        ordering = ('-date',)


class LogWorkContracts(models.Model):
    CONTRACT_TYPES = (
        ('постоянно', 'постоянно'),
        ('внешнее совместительство', 'внешнее совместительство'),
        ('внутреннее совместительство', 'внутреннее совместительство'),
        ('срочный', 'срочный')
    )
    STATUS_TYPES = (
        ('нет приказа', 'нет приказа'),
        ('номер занят', 'номер занят'),
        ('подшит', 'подшит')
    )
    company = models.ForeignKey(Companies, related_name='company_log_work_contracts', on_delete=models.PROTECT,
                                verbose_name='Компания', default=2)
    number = models.CharField('№', max_length=20)
    date = models.DateField('Дата', default=datetime.date.today)
    worker = models.ForeignKey(Workers, related_name='worker_log_work_contracts', on_delete=models.PROTECT,
                               verbose_name='Сотрудник')
    position_division = models.CharField('Должность/подразделение', max_length=200)
    contract_type = models.CharField('Вид договора', choices=CONTRACT_TYPES, max_length=50, default='нет приказа')
    status = models.CharField('Статус', choices=STATUS_TYPES, max_length=30, default='нет приказа')
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.number}: {self.worker} ({self.position_division}) автор: {self.author_created}'

    class Meta:
        verbose_name = 'Журнал регистрации трудовых договоров'
        verbose_name_plural = 'Журналы регистрации трудовых договоров'
        ordering = ('-number',)


class RegisterFinSupport(models.Model):
    GROUP_TYPES = (
        ('рабочий персонал', 'рабочий персонал'),
        ('специалист', 'специалист'),
        ('руководитель', 'руководитель')
    )
    AMOUNT_TYPES = (
        ('15 000', '15 000'),
        ('20 000', '20 000'),
        ('25 000', '25 000')
    )
    MONTH_TYPES = (
        (1, 'январь'),
        (2, 'февраль'),
        (3, 'март'),
        (4, 'апрель'),
        (5, 'май'),
        (6, 'июнь'),
        (7, 'июль'),
        (8, 'август'),
        (9, 'сентябрь'),
        (10, 'октябрь'),
        (11, 'ноябрь'),
        (12, 'декабрь')
    )
    STATUS_TYPES = (
        ('в ожидании', 'в ожидании'),
        ('выдано', 'выдано'),
        ('отказано', 'отказано')
    )
    company = models.ForeignKey(Companies, related_name='company_register_fin_support', on_delete=models.PROTECT,
                                verbose_name='Компания', default=2)
    worker = models.ForeignKey(Workers, related_name='worker_register_fin_support', on_delete=models.PROTECT,
                               verbose_name='Сотрудник')
    position = models.CharField('Должность', max_length=200)
    date_of_receipt = models.DateField('Дата приёма', default=datetime.date.today)
    group = models.CharField('Группа', choices=GROUP_TYPES, max_length=50, default='рабочий персонал')
    amount = models.CharField('Сумма', choices=AMOUNT_TYPES, max_length=50, default='15 000')
    month_of_issue = models.IntegerField('Месяц выдачи', choices=MONTH_TYPES, default=1)
    comments = models.CharField('Комментарии', max_length=250, blank=True)
    status = models.CharField('Статус', choices=STATUS_TYPES, max_length=30, default='в ожидании')
    date_of_document = models.DateField('Дата документа', default=datetime.date.today)
    author_created = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return f'{self.worker}: {self.position} ({self.amount}-{self.status}) автор: {self.author_created}'

    class Meta:
        verbose_name = 'Реестр выдачи материальной помощи'
        verbose_name_plural = 'Реестр выдачи материальной помощи'
        ordering = ('month_of_issue',)
