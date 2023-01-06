from django.urls import include, path
from rest_framework.routers import DefaultRouter
from applications.spam.views import SpamAPIView

router = DefaultRouter()

router.register('', SpamAPIView)

urlpatterns = [
    path('', include(router.urls))
]