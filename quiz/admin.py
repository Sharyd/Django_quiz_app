from django.contrib import admin
from .models import Quiz, Question, Option, Answer


# Register your models here.


class OptionInline(admin.TabularInline):
    model = Option

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            count = obj.options.count()
            return 4 - min(count, 4)
        return 4


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ("text", "quiz__title")
    list_filter = ("quiz",)
    list_display = ("text", "quiz")
    inlines = [OptionInline, AnswerInline]


class OptionAdmin(admin.ModelAdmin):
    search_fields = ("text", "question__text")
    list_filter = ("question__quiz",)
    list_display = ("text", "question")
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ("question__text", "correct_option__text")
    list_filter = ("question__quiz",)
    list_display = ("question", "correct_option")


admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Answer, AnswerAdmin)
