# models.py

from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings

class Balance(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='balance')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update_balance(self, change):
        self.amount += change
        self.save()

class AmountGiven(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='amounts_given')
    amount_given = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update the balance when amount is given
        balance, _ = Balance.objects.get_or_create(user=self.user)
        balance.update_balance(self.amount_given)

class Spend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='spends')
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    spent_on = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update the balance when amount is spent
        balance = Balance.objects.get(user=self.user)
        balance.update_balance(-self.amount_spent)
