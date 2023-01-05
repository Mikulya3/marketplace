
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from applications.parcer.serializers import ParcingSerializers


@api_view(["GET"])
def food_properties(request):
    if request.method == "GET":
        serializers = ParcingSerializers(data=request.data)
        serializers.is_valid()
        return Response(serializers.data, status=status.HTTP_200_OK)