from django.contrib import admin
from .models import Ai

@admin.register(Ai)
class AiAdmin(admin.ModelAdmin):
    list_display = ['title','created']
