from django import forms
from .models import MyCalendar
from django.db import models
from datetime import date
from django.forms import ModelForm

class MyCalendarForm(ModelForm):
    class Meta:
        model = MyCalendar
        fields = '__all__'
