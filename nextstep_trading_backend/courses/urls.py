from django.urls import path, include
from .views import ArticlesViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('article', ArticlesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
