from rest_framework import serializers

from file.models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'


class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('file',)
