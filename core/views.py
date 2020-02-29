# from django.core import serializers
# from django.http import HttpResponse
# from django.shortcuts import render
# from rooms.models import Room

# def list_rooms(request):
#     # import json을 해서 for문으로 queryset을 json에 넣으려고 해도 안된다.
#     # 그래서 serializer를 사용해야 한다.
#     data = serializers.serialize("json", Room.objects.all())
#     response = HttpResponse(content=data)
#     return response
