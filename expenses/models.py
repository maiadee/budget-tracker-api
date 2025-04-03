from django.db import models
from budget.models import Budget
from users.models import User

# Create your models here.
class Expense(models.Model):

    CATEGORY_CHOICES = [
        ("bills", "Bills"),
        ("groceries", "Groceries"),
        ("shopping", "Shopping"),
        ("savings", "Savings"),
        ("health_beauty", "Health & Beauty"),
        ("holiday", "Holiday"),
        ("entertainment", "Entertainment"),
        ("car_travel", "Car & Travel"),
        ("household_items", "Household Items"),
        ("pets", "Pets"),
    ]

    budget = models.ForeignKey(Budget, related_name='expenses', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="misc")

    def save(self, *args, **kwargs):
        """
        Override the save method to update the total_spent of the associated budget.
        """
        # Save the Expense first
        super().save(*args, **kwargs)
        
        # After saving the Expense, update the total_spent of the associated Budget
        self.update_budget_total_spent()

    def delete(self, *args, **kwargs):
        """
        Override the delete method to update the total_spent of the associated budget
        after deleting an expense.
        """
        # Save the budget before deleting the expense
        self.update_budget_total_spent()
        
        # Call the parent class's delete method to delete the Expense
        super().delete(*args, **kwargs)

    def update_budget_total_spent(self):
        """
        Update the total_spent field for the associated budget.
        This will be called whenever an expense is saved or deleted.
        """
        if self.budget:
            # Recalculate the total_spent for the associated Budget
            self.budget.total_spent = sum(exp.amount for exp in self.budget.expenses.all())
            # Save the updated Budget object
            self.budget.save()

    def __str__(self):
        return f"{self.name}: ${self.amount} - {self.category}"