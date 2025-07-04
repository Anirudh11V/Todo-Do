from django.http import Http404
from django.shortcuts import get_object_or_404
from apptodo.models import todotask

from .serializers import todoSerializer

from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
# Create your views here.

class TodoViewset(viewsets.ViewSet):
    def list(self, request):
        query = todotask.objects.all()
        serial = todoSerializer(query, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serial = todoSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        query = get_object_or_404(todotask, pk = pk)
        serial = todoSerializer(query)
        return Response(serial.data, status= status.HTTP_200_OK)

    def update(self, request, pk=None):
        query = get_object_or_404(todotask, pk= pk)
        serial = todoSerializer(query, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk= None):
        query = get_object_or_404(todotask, pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)