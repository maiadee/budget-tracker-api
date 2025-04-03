from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Budget
from expenses.models import Expense

@receiver(post_save, sender=Expense)
def update_budget_total_spent_on_save(sender, instance, **kwargs):
    # Whenever an expense is saved, recalculate the total_spent for the associated budget
    instance.update_budget_total_spent()

@receiver(post_delete, sender=Expense)
def update_budget_total_spent_on_delete(sender, instance, **kwargs):
    # When an expense is deleted, recalculate the total_spent for the associated budget
    instance.update_budget_total_spent()
