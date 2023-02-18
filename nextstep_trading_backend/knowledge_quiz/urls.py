from django.urls import path, include
from .views import QuizQuestionsViewSet, QuizViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('quiz_questions', QuizQuestionsViewSet)
router.register('quiz', QuizViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
