from django.contrib import admin

from .models import *

admin.site.register(Question)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(FillInTheBlankQuestion)
admin.site.register(TranslateQuestion)
admin.site.register(LessonCategory)
admin.site.register(ListenQuestion)