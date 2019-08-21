from rest_framework import serializers
from .models import UserAddress, UserMessage, UserIntegrate


class AddressSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = UserAddress
        fields = ("id", "user", "province", "city", "district", "street", "address", "phone", "add_time")


class MessageSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = UserMessage
        fields = ("user", "message_type", "title", "message", "file", "id", "add_time")


class UserIntegrateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserIntegrate
        fields = ("user", "integrate_time", "source", "expiry_day")


