from rest_framework.generics import ListAPIView, RetrieveAPIView # ListAPIView
from rest_framework.views import APIView # CBV
from rest_framework.decorators import api_view # FBV
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer

# ListAPIView
class ListRoomsView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SeeRoomView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# Class Based View
# class ListRoomsView(APIView):
#     def get(self, requset):
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms, many=True)
#         return Response(serializer.data)
        
#     def post(self, request):
#         pass

# Function Based View
# # @api_view(["GET", "DELETE"])
# @api_view(["GET"])
# def list_rooms(request):
#     rooms = Room.objects.all()
#     serialized_rooms = RoomSerializer(rooms, many=True)
#     return Response(data=serialized_rooms.data)