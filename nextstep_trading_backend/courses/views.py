from rest_framework import viewsets
from .serializers import Articles, ArticlesSerializer


# Create your views here.

class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
