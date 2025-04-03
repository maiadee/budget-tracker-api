from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'total_budget', 'total_spent', 'total_left']