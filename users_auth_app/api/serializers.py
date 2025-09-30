from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from users_auth_app.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("fullname", "email", "password", "repeated_password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if data["password"] != data["repeated_password"]:
            raise serializers.ValidationError("Passwörter stimmen nicht überein.")
        return data

    def create(self, validated_data):
        validated_data.pop("repeated_password")
        user = User.objects.create_user(**validated_data)
        return user

class EmailCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "fullname"]

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Kein User mit dieser E-Mail gefunden.")
        return value
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError("Ungültige Zugangsdaten.")

        if not user.check_password(data["password"]):
            raise serializers.ValidationError("Ungültige Zugangsdaten.")

        data["user"] = user
        return data

