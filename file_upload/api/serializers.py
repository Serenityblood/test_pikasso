from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    """Сериализатор модели файла"""
    class Meta:
        model = File
        fields = ['file', 'uploaded_at', 'processed',]
