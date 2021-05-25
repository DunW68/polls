from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class AdminChoice(admin.TabularInline):
    model = Choice

class AdminQuestion(admin.ModelAdmin):
    list_filter = ['pub_date']
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    inlines = [AdminChoice]
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, AdminQuestion)