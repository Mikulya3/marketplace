from rest_framework.routers import DefaultRouter
from applications.product.views import ProductAPIView, CategoryAPIView, RecommendationAPIView
from django.urls import path, include

router = DefaultRouter()
router.register('recommend', RecommendationAPIView)
router.register('category', CategoryAPIView)
router.register('', ProductAPIView)


urlpatterns = [
    path('', include(router.urls)),
]