from django.db import models
from django.contrib.auth.models import User
from users.models import User

# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey(TO=User, related_name='budgets', on_delete=models.CASCADE)
    total_budget = models.FloatField()
    total_spent = models.FloatField(default=0.0)
    
    @property
    def total_left(self):
        # Dynamically calculate the remaining budget - this is more efficient because it doesn't store the value, but calculates it on the fly.
        return self.total_budget - self.total_spent

    def __str__(self):
        return f"Budget for {self.user.username}: ${self.total_budget}, Spent: ${self.total_spent}, Left: ${self.total_left}"