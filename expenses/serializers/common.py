from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'