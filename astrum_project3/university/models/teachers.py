from django.db import models
from .subjects import Subject
from .groups import Group


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject)
    group = models.ForeignKey(Group)

    def __str__(self):
        return f"{self.name} {self.subject}dan {self.group}ga dars beradi."
