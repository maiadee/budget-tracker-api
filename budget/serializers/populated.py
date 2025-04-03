from .common import BudgetSerializer
from expenses.serializers.common import ExpenseSerializer

class PopulatedBudgetSerializer(BudgetSerializer):
    expenses = ExpenseSerializer(many=True, read_only=True)