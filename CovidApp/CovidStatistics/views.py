from django.shortcuts import render
from transliterate import translit

import requests
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.views import APIView
from CovidStatistics.models import CovidData

from CovidStatistics.serializers import CovidDataPostSerializer,CovidDataGetSerializer


class CovidDataViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    serializer_class = CovidDataPostSerializer
    permission_classes = [AllowAny,]
    queryset = CovidData.objects.all()

    def get_serializer_class(self):
        serializer_class = CovidDataPostSerializer
        if self.action == 'create':
            serializer_class = CovidDataPostSerializer
        elif self.action =='list':
            serializer_class = CovidDataGetSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        try:
            test = CovidData.objects.all()
            test.delete()
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




