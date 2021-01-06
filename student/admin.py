from django.contrib import admin
from student.models import Class,Com_subj_class,ID,result,student,subject
# Register your models here.

admin.site.register(Class.StudentClass)
admin.site.register(ID.Student_ID)
admin.site.register(student.Student)
admin.site.register(subject.Subject)
admin.site.register(Com_subj_class.SubjectCombination)
admin.site.register(result.DeclareResult)