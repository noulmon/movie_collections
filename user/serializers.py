''' Service class provides the encapsulates the business logic '''

from django.db import transaction
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, min_length=6)
    password = serializers.CharField(required=True, allow_blank=False, min_length=8)

    @transaction.atomic()
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        # checking whether user already exists or not
        user = User.objects.get_or_create(username=username)
        if not user[1]:
            # raising validation error if user already exists
            raise serializers.ValidationError('User already exist. Please login or try a different username')
        # setting password if user is new
        user[0].set_password(password)
        user[0].save()
        return user[0]
