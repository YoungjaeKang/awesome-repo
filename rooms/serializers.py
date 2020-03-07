from rest_framework import serializers
from .models import Room
from users.serializers import UserSerializer


# class RoomSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=140)
#     price = serializers.IntegerField()
#     bedrooms = serializers.IntegerField()
#     instant_book = serializers.BooleanField()


# Magic !
class ReadRoomSerializer(serializers.ModelSerializer):
    # RoomSerializer의 user가 id(int)로 나오는데 그거 말고 username이랑 superhost를 보고 싶다면
    # user에도 serializers.py와 class를 만들고 그걸 여기서 import해준다.
    user = UserSerializer()

    class Meta:
        model = Room
        # fields = ("pk", "name", "price", "user",)
        exclude = ("modified",)


# Manual
class WriteRoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)
    address = serializers.CharField(max_length=140)
    price = serializers.IntegerField(help_text="USD per night")
    beds = serializers.IntegerField(default=1)
    lat = serializers.DecimalField(max_digits=10, decimal_places=6)
    lng = serializers.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = serializers.IntegerField(default=1)
    bathrooms = serializers.IntegerField(default=1)
    check_in = serializers.TimeField(default="00:00:00")
    check_out = serializers.TimeField(default="00:00:00")
    instant_book = serializers.BooleanField(default=False)