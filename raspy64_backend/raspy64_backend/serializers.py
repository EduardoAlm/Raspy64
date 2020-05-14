import json

from django.utils import timezone
from rest_framework import serializers

from .models import Users


class userSerializer(serializers.Serializer):
    Nome = serializers.CharField(required=True)
    Email = serializers.CharField(required=True)
    Telemovel = serializers.IntegerField(required=True)
    Raspadinha = serializers.IntegerField(required=True)

    def validate(self, attrs):
        """
        Validate the model attributes
        """
        for attr in attrs:
            print(attr)
        return attrs

    def create(self, validated_data):
        """
        Create the model object
        """
        newuser = User(**validated_data)
        newuser.save()
        return newuser
