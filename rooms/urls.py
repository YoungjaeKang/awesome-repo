from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from . import viewsets

app_name = "rooms"

# viewsets.py
router = DefaultRouter()
router.register("", viewsets.RoomViewset, basename='room')

urlpatterns = router.urls


# CBV
# urlpatterns = [
#     path("list/", views.ListRoomsView.as_view()),
#     path("<int:pk>/", views.SeeRoomView.as_view()),
# ]



# FBV
# urlpatterns = [path("list/", views.list_rooms)]
