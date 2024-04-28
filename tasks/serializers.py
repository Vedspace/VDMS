from rest_framework import serializers
from .models import Task, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_by']

class TaskSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all(), required=False)
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), required=False)
    completed_by = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'upload_date', 'priority', 'assigned_to', 'completed', 'completed_by', 'task_done', 'completion_date', 'deadline', 'category']
        read_only_fields = ['upload_date', 'completed', 'completed_by']

    def update(self, instance, validated_data):
        instance.completed = validated_data.get('completed', instance.completed)
        if validated_data.get('completed'):
            instance.completed_by = self.context['request'].user
        instance.save()
        return instance
