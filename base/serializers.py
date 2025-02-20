from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    age = serializers.IntegerField()
    
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Name must contain only alphabetic characters.")
        return value

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Email must contain '@' symbol.")
        return value

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("This person is not born")
        return value