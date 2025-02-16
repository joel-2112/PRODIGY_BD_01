from rest_framework import serializers
from .models import User
from django.core.validators import validate_email 
from django.core.exceptions import ValidationError as DjangoValidationError
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age']
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                detail="Name must contain only alphabetic characters.",
                code='invalid_name'
            )
        return value

    def validate_email(self, value):
        # Use Django's built-in email validation
        try:
            validate_email(value)
        except DjangoValidationError:
            raise serializers.ValidationError(
                detail="Invalid email address.",
                code='invalid_email'
            )
        return value
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError(
                detail="Age must be a positive integer.",
                code='invalid_age'
            )
        return value