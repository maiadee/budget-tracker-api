from django.apps import AppConfig


class ExpensesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expenses'

    def ready(self):
        import expenses.signals  # Import the signals when the app is ready