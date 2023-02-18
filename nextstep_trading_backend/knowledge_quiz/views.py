from rest_framework import viewsets
from .serializers import QuizQuestionsSerializer, QuizQuestions, Quiz, QuizSerializer


# Create your views here.

class QuizQuestionsViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestions.objects.all()
    serializer_class = QuizQuestionsSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
