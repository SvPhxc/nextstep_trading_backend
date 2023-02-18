from django.urls import path
from .views import BusinessViewSet, CryptoNewsViewSet, StocksNewsViewSet, ForexNewsViewSet

urlpatterns = [
    path('', BusinessViewSet.as_view()),
    path('crypto/', CryptoNewsViewSet.as_view()),
    path('stocks/', StocksNewsViewSet.as_view()),
    path('forex/', ForexNewsViewSet.as_view()),

]
