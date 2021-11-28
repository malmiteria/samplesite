from django.db import models

from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Sudoku(models.Model):
    cells = ArrayField(ArrayField(models.IntegerField(blank=True), size=9), size=9)


