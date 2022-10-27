from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Author'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
