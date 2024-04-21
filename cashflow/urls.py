# urls.py

from django.urls import path
from .views import AmountGivenListCreate, AmountGivenRetrieveUpdateDestroy, SpendListCreate, SpendRetrieveUpdateDestroy, BalanceListCreate, BalanceRetrieveUpdateDestroy

urlpatterns = [
    path('amount-given/', AmountGivenListCreate.as_view(), name='amount-given-list-create'),
    path('amount-given/<int:pk>/', AmountGivenRetrieveUpdateDestroy.as_view(), name='amount-given-detail'),
    path('spend/', SpendListCreate.as_view(), name='spend-list-create'),
    path('spend/<int:pk>/', SpendRetrieveUpdateDestroy.as_view(), name='spend-detail'),
    path('balance/', BalanceListCreate.as_view(), name='balance-list-create'),
    path('balance/<int:pk>/', BalanceRetrieveUpdateDestroy.as_view(), name='balance-detail'),
]
