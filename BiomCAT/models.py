from django.db import models
from django.contrib.auth.models import User

class ControlGroup(models.Model):
    name = models.CharField(max_length=100)

class TestSubject(models.Model):
    user = models.OneToOneField(User)
    control_group = models.ForeignKey(ControlGroup)
    roll_no = models.IntegerField()
    age = models.PositiveIntegerField(default=20)
    completed_survey = models.BooleanField(default=False)
    current_question = models.IntegerField(default=0)

class Question(models.Model):
    CORRECT_SUBJECT_CHOICES = (
        ('R', 'Red'),
        ('G', 'Green'),
        ('B', 'Blue'),
        ('Y', 'Yellow'),
    )
    correct_subject = models.CharField(max_length=1, choices=CORRECT_SUBJECT_CHOICES)