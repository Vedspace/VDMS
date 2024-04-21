# admin.py

from django.contrib import admin
from .models import AmountGiven, Spend, Balance

class AmountGivenAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount_given']
    search_fields = ['user__username']  # Assuming 'username' is the relevant user identifier
    list_filter = ['user']  # Filter records by user

class SpendAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount_spent', 'spent_on']
    search_fields = ['user__username', 'spent_on']  # Enable searching by username and where the money was spent
    list_filter = ['user', 'spent_on']  # Filter by user and spent_on category

class BalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount']
    search_fields = ['user__username']  # Enable searching by username
    list_filter = ['user']  # Filter records by user

admin.site.register(AmountGiven, AmountGivenAdmin)
admin.site.register(Spend, SpendAdmin)
admin.site.register(Balance, BalanceAdmin)
