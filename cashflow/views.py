from rest_framework import generics, permissions
from .models import AmountGiven, Spend,Balance
from .serializers import AmountGivenSerializer, SpendSerializer, BalanceSerializer

class AmountGivenListCreate(generics.ListCreateAPIView):
    queryset = AmountGiven.objects.all()
    serializer_class = AmountGivenSerializer

class AmountGivenRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AmountGiven.objects.all()
    serializer_class = AmountGivenSerializer

class SpendListCreate(generics.ListCreateAPIView):
    queryset = Spend.objects.all()
    serializer_class = SpendSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure user is logged in

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

class SpendRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spend.objects.all()
    serializer_class = SpendSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure user is logged in

class BalanceListCreate(generics.ListCreateAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

class BalanceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer