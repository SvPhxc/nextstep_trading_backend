from django.contrib import admin
from .models import Articles


# Register your models here.

@admin.register(Articles)
class Articles(admin.ModelAdmin):
    list_display = ('title', 'knowledge_level')
