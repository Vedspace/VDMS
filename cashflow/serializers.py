from rest_framework import serializers
from .models import AmountGiven, Spend, Balance

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['user', 'amount']
class AmountGivenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmountGiven
        fields = ['id', 'user', 'amount_given', 'amount_remaining']

class SpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spend
        fields = ['id', 'amount_spent', 'spent_on']
        read_only_fields = ['id', 'user']  # Make 'left_money' and 'user' read-only

    def create(self, validated_data):
        # Set the user from the request to the Spend model
        validated_data['user'] = self.context['request'].user
        return Spend.objects.create(**validated_data)
