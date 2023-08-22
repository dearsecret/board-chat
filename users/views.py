from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PrivateUserSerializer

# Create your views here.


class ListUser(APIView):
    def get(self, request):
        print(f"{request.data}")
        user = request.user
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)
