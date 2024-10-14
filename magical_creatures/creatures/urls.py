from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MagicalCreatureViewSet

router = DefaultRouter()
router.register(r'creatures', MagicalCreatureViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
