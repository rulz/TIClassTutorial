from django import forms
from .models import MyCalendar
from django.db import models
from datetime import date
from django.forms import ModelForm
from django.contrib.auth.models import User

class MyCalendarForm(ModelForm):
    class Meta:
        model = MyCalendar
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
