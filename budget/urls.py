from django.urls import path
from .views import ClearBudgetView, CreateBudgetView

urlpatterns = [
    path('clear/', ClearBudgetView.as_view(), name='clear_budget'),
    path('create/', CreateBudgetView.as_view(), name='create_budget'),
]