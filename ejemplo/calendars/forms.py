from django import forms
from .models import MyCalendar
from django.db import models
from datetime import date


class MyCalendarForm(forms.Form):
    class Meta:
        model = MyCalendar
        fields = '__all__'
