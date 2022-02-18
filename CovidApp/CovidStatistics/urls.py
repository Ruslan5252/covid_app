from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import CovidDataViewSet
router = DefaultRouter()
router.register('',CovidDataViewSet)
urlpatterns = [

    ]+router.urls