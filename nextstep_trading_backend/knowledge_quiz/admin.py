from django.contrib import admin
from .models import QuizQuestions, Quiz


# Register your models here.


@admin.register(Quiz)
class Quiz(admin.ModelAdmin):
    list_display = ('title', 'article_id')


@admin.register(QuizQuestions)
class QuizQuestions(admin.ModelAdmin):
    list_display = ('question', 'quiz_id',)
