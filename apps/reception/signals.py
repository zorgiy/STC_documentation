from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from apps.reception.models import Incoming, Outgoing, Order


@receiver(pre_save, sender=Incoming)
def create_and_update_incoming_index(sender, instance, **kwargs):
    if not instance.pk:
        company = instance.company
        author = instance.author
        current_year = timezone.now().year
        if company.last_document_year != current_year:
            company.last_document_year = current_year
            company.last_document_number_incoming = 0
        last_document_number = company.last_document_number_incoming + 1
        instance.index = f"{last_document_number:03}-{company.index}-{author.id}-{current_year}"
        company.last_document_number_incoming = last_document_number
        company.save()
    else:
        company = instance.company
        author = instance.author
        current_year = int(instance.index.split('-')[-1])
        # Если изменяем author у документов прошлых лет, то год не меняем, а автора в index меняем
        if company.last_document_year != current_year:
            instance.index = f"{instance.index.split('-')[0]}-{company.index}-{author.id}-{current_year}"
        else:
            old_instance = Incoming.objects.get(pk=instance.pk)
            # Если изменения не затрагивают компанию и автора, то ничего не делаем
            if old_instance.company == instance.company and old_instance.author == instance.author:
                return
            # Если документ перенесли в другую компанию, то обновляем номера обеих компаний
            if old_instance.company != instance.company:
                old_company = old_instance.company
                old_company_last_number = old_company.last_document_number_incoming
                company_index = instance.company.index
                last_document_number = instance.company.last_document_number_incoming + 1
                instance.index = f"{last_document_number:03}-{company_index}-{author.id}-{current_year}"
                instance.company.last_document_number_incoming = last_document_number
                instance.company.save()
                old_company.last_document_number_incoming = old_company_last_number - 1
                old_company.save()
            # Если изменился только автор, то обновляем только номер документа
            elif old_instance.author != instance.author:
                instance.index = f"{instance.index.split('-')[0]}-{company.index}-{author.id}-{current_year}"


@receiver(post_delete, sender=Incoming)
def delete_incoming_index(sender, instance, **kwargs):
    company = instance.company
    # Находим последний документ Incoming для данной компании (исключая удаляемый документ)
    last_incoming = Incoming.objects.filter(company=company).exclude(id=instance.id).order_by('-id').first()
    if last_incoming:
        # Извлекаем номер последнего документа из индекса последнего входящего документа
        last_number = int(last_incoming.index.split('-')[0])
    else:
        last_number = 0
    company.last_document_number_incoming = last_number
    company.save()


@receiver(pre_save, sender=Outgoing)
def create_and_update_outgoing_index(sender, instance, **kwargs):
    if not instance.pk:
        company = instance.company
        author = instance.author
        current_year = timezone.now().year
        if company.last_document_year != current_year:
            company.last_document_year = current_year
            company.last_document_number_outgoing = 0
        last_document_number = company.last_document_number_outgoing + 1
        instance.index = f"{company.index}-{author.id}-{current_year}-{last_document_number:03}"
        company.last_document_number_outgoing = last_document_number
        company.save()
    else:
        company = instance.company
        author = instance.author
        current_year = int(instance.index.split('-')[-2])
        if company.last_document_year != current_year:
            instance.index = f"{company.index}-{author.id}-{current_year}-{instance.index.split('-')[-1]:03}"
        else:
            old_instance = Outgoing.objects.get(pk=instance.pk)
            if old_instance.company == instance.company and old_instance.author == instance.author:
                return
            if old_instance.company != instance.company:
                old_company = old_instance.company
                old_company_last_number = old_company.last_document_number_outgoing
                company_index = instance.company.index
                last_document_number = instance.company.last_document_number_outgoing + 1
                instance.index = f"{company_index}-{author.id}-{current_year}-{last_document_number:03}"
                instance.company.last_document_number_outgoing = last_document_number
                instance.company.save()
                old_company.last_document_number_outgoing = old_company_last_number - 1
                old_company.save()
            elif old_instance.author != instance.author:
                instance.index = f"{company.index}-{author.id}-{current_year}-{instance.index.split('-')[-1]:03}"


@receiver(post_delete, sender=Outgoing)
def delete_outgoing_index(sender, instance, **kwargs):
    company = instance.company
    last_outgoing = Outgoing.objects.filter(company=company).exclude(id=instance.id).order_by('-id').first()
    if last_outgoing:
        last_number = int(last_outgoing.index.split('-')[-1])
    else:
        last_number = 0
    company.last_document_number_outgoing = last_number
    company.save()


@receiver(pre_save, sender=Order)
def create_and_update_order_index(sender, instance, **kwargs):
    if not instance.pk:
        company = instance.company
        year_now = timezone.now().year
        if company.last_document_year != year_now:
            company.last_document_number_order = 0
        company.last_document_number_order += 1
        instance.number = f"{company.index}-{company.last_document_number_order:03}"
        company.last_document_year = year_now
        company.save(update_fields=['last_document_number_order', 'last_document_year'])
    else:
        original_instance = sender.objects.get(pk=instance.pk)
        if original_instance.company.index != instance.company.index:
            old_company = original_instance.company
            new_company = instance.company
            old_company.last_document_number_order -= 1
            old_company.save(update_fields=['last_document_number_order'])
            new_company.last_document_number_order += 1
            new_company.save(update_fields=['last_document_number_order'])
            instance.number = f"{new_company.index}-{new_company.last_document_number_order:03}"


@receiver(post_delete, sender=Order)
def delete_order_index(sender, instance, **kwargs):
    company = instance.company
    last_order = Order.objects.filter(company=company).exclude(id=instance.id).order_by('-id').first()
    if last_order:
        last_number = int(last_order.number.split('-')[-1])
    else:
        last_number = 0
    company.last_document_number_order = last_number
    company.save()
