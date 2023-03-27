from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.transactions'

    def ready(self):
        import applications.transactions.signals
