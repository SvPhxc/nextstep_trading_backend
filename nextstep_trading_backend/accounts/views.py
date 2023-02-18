from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import AppUser
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userdata(request):
    user = request.user
    user_info = user.objects.get()
    serializer = UserSerializer
    return Response(serializer.data)
