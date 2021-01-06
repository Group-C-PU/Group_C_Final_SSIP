from django.db import models
from django.urls import reverse

class StudentClass(models.Model):
    class_name              =   models.CharField(max_length=100, help_text='Eg- IT 19, IT 20, MGT 20 etc')
    section                 =   models.CharField(max_length=10, help_text='Eg- 1, 2, 3 etc')
    creation_date           =   models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('class_list')

    def __str__(self):
        return "%s Section-%s"%(self.class_name, self.section)
