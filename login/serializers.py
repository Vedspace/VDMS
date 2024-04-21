from rest_framework import serializers
from .models import DeviceToken

class DeviceTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceToken
        fields = ['token']

    def create(self, validated_data):
        user = self.context['request'].user
        token, created = DeviceToken.objects.update_or_create(
            user=user,
            defaults={'token': validated_data['token']}
        )
        return token
