from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "choices"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]

    def choices(self, obj):
        return ", ".join([c.choice_text for c in obj.choices.all()])


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
