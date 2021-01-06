from django.db import models
from django.urls import reverse

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.IntegerField()
    subject_creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    subject_update_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.subject_name
    
    def get_absolute_url(self):
        return reverse('subject_list')




    
