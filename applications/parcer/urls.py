from django.urls import path

from .views import food_properties


urlpatterns = [
    path('api/', food_properties)
]