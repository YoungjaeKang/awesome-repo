from rest_framework import serializers
from .models import Room
from users.serializers import TinyUserSerializer


# class RoomSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=140)
#     price = serializers.IntegerField()
#     bedrooms = serializers.IntegerField()
#     instant_book = serializers.BooleanField()

class RoomSerializer(serializers.ModelSerializer):
    # RoomSerializer의 user가 id(int)로 나오는데 그거 말고 username이랑 superhost를 보고 싶다면
    # user에도 serializers.py와 class를 만들고 그걸 여기서 import해준다.
    user = TinyUserSerializer()

    class Meta:
        model = Room
        fields = ("pk", "name", "price", "user",)


class BigRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ()