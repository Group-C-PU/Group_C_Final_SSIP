from django.db import models
from django.urls import reverse
from student.models.Class import StudentClass
from student.models.subject import Subject

class SubjectCombination(models.Model):
    select_class = models.ForeignKey(StudentClass,on_delete=models.CASCADE)
    select_subject = models.ManyToManyField(Subject)

    def get_absolute_url(self):
        return reverse('subject_combination_list')

    def __str__(self):
        return '%s Section-%s'%(self.select_class.class_name, self.select_class.section)