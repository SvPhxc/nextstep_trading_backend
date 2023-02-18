from django.db import models
from nextstep_trading_backend.courses.models import Articles


# Create your models here.

class Quiz(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
    )
    article_id = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE,
    )


class QuizQuestions(models.Model):
    quiz_id = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
    )

    question = models.CharField(
        max_length=500,
        null=False,
    )
    option1 = models.CharField(
        max_length=200,
        null=False,
    )
    option2 = models.CharField(
        max_length=200,
        null=False,
    )
    option3 = models.CharField(
        max_length=200,
        null=False,
    )
    option4 = models.CharField(
        max_length=200,
        null=False,
    )
    rightAnswer = models.CharField(
        max_length=200,
        null=False,
    )
    choice = models.CharField(
        max_length=200,
        null=True,
    )
    points = models.IntegerField(
        null=False,
    )

