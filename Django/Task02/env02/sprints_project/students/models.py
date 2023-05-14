from django.db import models

class Student(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    mobile_no = models.IntegerField()

class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    course_duration = models.IntegerField()
    course_code = models.CharField(max_length=255)
# Create your models here.
