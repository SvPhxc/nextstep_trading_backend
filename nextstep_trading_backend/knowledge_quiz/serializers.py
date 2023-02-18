from rest_framework import serializers
from .models import QuizQuestions, Quiz


class QuizQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestions
        fields = ['id', 'quiz_id', 'question', 'option1', 'option2', 'option3', 'option4', 'rightAnswer', 'choice',
                  'points', ]


class QuizSerializer(serializers.ModelSerializer):
    quiz_questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'article_id', 'quiz_questions', ]

    def get_quiz_questions(self, obj):
        quiz_id = obj.id
        questions = QuizQuestions.objects.filter(quiz_id=quiz_id)
        serializer = QuizQuestionsSerializer(questions, many=True)
        return serializer.data
