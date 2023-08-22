from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"^ws/boards/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
