from django.db import models
from django.urls import reverse

class Student_ID(models.Model):
    student_num = models.CharField(max_length=5,help_text='00001,00002, etc.')

    def get_absolute_url(self):
        return reverse('id_create')

    def __str__(self):
        return self.student_num