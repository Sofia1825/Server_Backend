from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgricultorViewSet

router = DefaultRouter()
router.register(r'agricultores', AgricultorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]