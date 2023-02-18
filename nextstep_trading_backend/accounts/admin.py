from django.contrib import admin
from .models import AppUser


# Register your models here.

# Samuil
# qgupKe7FjuH(k@hn

@admin.register(AppUser)
class AppUser(admin.ModelAdmin):
    fields = ['user_knowledge_level', 'credit_coins', ]
    list_display = ('username', 'user_knowledge_level', 'credit_coins',)
    list_display_links = ('username', )
