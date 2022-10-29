from django.db import models
from .subjects import Subject
from .groups import Group
from .teachers import Teacher


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject)
    group = models.ForeignKey(Group)
    teachers = models.ForeignKey(Teacher)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"