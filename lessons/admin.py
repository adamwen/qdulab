from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from lessons.models import Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_person', 'place', 'time', 'created_at')

admin.site.register(Lesson, LessonAdmin)

