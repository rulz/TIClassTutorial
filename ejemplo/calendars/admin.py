from django.contrib import admin
from .models import MyCalendar


@admin.register(MyCalendar)
class MyCalendarAdmin(admin.ModelAdmin):
    pass
    #list_display = ('class_name')