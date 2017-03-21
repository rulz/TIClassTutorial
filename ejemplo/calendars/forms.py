from django import forms

from .models import MyCalendar


class MyCalendarForm(forms.ModelForm):

    class Meta:
        model = MyCalendar
        fields = ['user', 'class_name', 'class_date', 'note', 'date_create', 'date_edit']