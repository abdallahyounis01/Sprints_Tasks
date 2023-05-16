from django.db import models


class Post(models.Model):
    Male = 'M'
    Female = 'F'
    GENDER_CHOICES = ((Male, 'Male'), (Female, 'Female'))
    username = models.CharField(max_length=255, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=Female)
    time = models.DateTimeField(auto_now_add=True)
