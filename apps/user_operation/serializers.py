from rest_framework import serializers
from .models import UserAddress


class AddressSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    add_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = UserAddress
        fields = ("user", "province", "city", "district", "street","address", "phone", "add_time")