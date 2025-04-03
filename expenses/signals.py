from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Expense
from budget.models import Budget

@receiver(post_save, sender=Expense)
def update_budget_total_spent_on_save(sender, instance, **kwargs):
    instance.update_budget_total_spent()

@receiver(post_delete, sender=Expense)
def update_budget_total_spent_on_delete(sender, instance, **kwargs):
    instance.update_budget_total_spent()
