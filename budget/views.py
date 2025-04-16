from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Budget

from .serializers.common import BudgetSerializer
from .serializers.populated import PopulatedBudgetSerializer

# Create your views here.
class CreateBudgetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Initialize the serializer with the data from the request
        budget_serializer = BudgetSerializer(data=request.data)
        if budget_serializer.is_valid():
            # Assign the authenticated user to the budget
            budget_serializer.save(user=request.user)
            return Response(budget_serializer.data, status=201)
        return Response(budget_serializer.errors, status=400)



class ClearBudgetView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        try:
             # Get the user's active budget (the one that has not been cleared)
            budget = Budget.objects.get(user=request.user, total_spent__gt=0) # Make sure there is an active budget with spending
            budget.clear_budget()
            return Response({"detail": "Budget has been cleared for the next month."}, status=200)
        except Budget.DoesNotExist:
            return Response ({"detail": "No budget found to clear."}, status=404)