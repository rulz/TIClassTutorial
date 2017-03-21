from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class MyCalendar(models.Model):
    user = models.ForeignKey(User)
    class_name = models.CharField(max_length=150)
    class_url = models.URLField()
    class_date = models.DateField()
    note = models.TextField()
    date_create = models.DateField()
    date_edit = models.DateField()

    class Meta:
        ordering = ('id', )


    def __str__(self):
        return self.user.username
