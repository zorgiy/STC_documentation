from django.apps import AppConfig


class ReceptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.reception'
    verbose_name = 'Приёмная'

    def ready(self):
        import apps.reception.signals
