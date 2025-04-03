from django.apps import AppConfig


class BudgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'budget'

    def ready(self):
        import budget.signals  # Import the signals when the app is ready