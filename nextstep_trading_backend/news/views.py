from rest_framework.views import APIView
from newsdataapi import NewsDataApiClient
from rest_framework.response import Response


class BusinessViewSet(APIView):
    def get(self, request):
        api = NewsDataApiClient(apikey="pub_15089662a152655e36a1709bc0e27d62196c5")
        # You can pass empty or with request parameters {ex. (country = "us")}
        response = api.news_api(q="business", country="us")
        return Response(response)


class CryptoNewsViewSet(APIView):
    def get(self, request):
        api = NewsDataApiClient(apikey="pub_15089662a152655e36a1709bc0e27d62196c5")
        # You can pass empty or with request parameters {ex. (country = "us")}
        response = api.news_api(q="crypto", country="us")
        return Response(response)


class StocksNewsViewSet(APIView):
    def get(self, request):
        api = NewsDataApiClient(apikey="pub_15089662a152655e36a1709bc0e27d62196c5")
        # You can pass empty or with request parameters {ex. (country = "us")}
        response = api.news_api(q="stocks", country="us")
        return Response(response)


class ForexNewsViewSet(APIView):
    def get(self, request):
        api = NewsDataApiClient(apikey="pub_15089662a152655e36a1709bc0e27d62196c5")
        # You can pass empty or with request parameters {ex. (country = "us")}
        response = api.news_api(q="forex", country="us")
        return Response(response)
