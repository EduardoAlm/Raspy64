import json

from django.utils import timezone
from rest_framework import serializers

from .models import Users


class userSerializer(serializers.Serializer):
    Telemovel = serializers.CharField(required=True)
    Username = serializers.CharField(required=True)
    Raspadinha = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        """
        Override
        """
        print("This is an update.")
        pass

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
        user = Users(**validated_data)
        user.save()
        return user
