from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='name', queryset=User.objects.all(), required=False)
    completed_by = serializers.SlugRelatedField(slug_field='name', read_only=True)
    is_completed = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'upload_date', 'priority', 'assigned_to', 'completed', 'completed_by', 'is_completed', 'task_done','completion_date','deadline']
        read_only_fields = ['upload_date', 'completed', 'completed_by']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if 'request' in self.context and not self.context['request'].user.is_staff:
            ret.pop('assigned_to', None)
        ret.pop('is_completed', None)
        return ret

    def update(self, instance, validated_data):
        is_completed = validated_data.pop('is_completed', None)
        if is_completed:
            instance.completed = True
            instance.completed_by = self.context['request'].user
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
