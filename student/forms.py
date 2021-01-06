from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models.ID import Student_ID
from .models.student import Student
from .models.result import DeclareResult
from .models.Class import StudentClass
from .models.subject import Subject 
from .models.Com_subj_class import SubjectCombination

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class IDForm(forms.ModelForm):
    class Meta:
        model=Student_ID
        fields ='__all__'
        widgets={'student_num':forms.TextInput(attrs={'class':'form-control'}),}
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['student_reg']
        widgets = {
            'student_id'  :  forms.Select(attrs={'class':'form-control'}),
            'student_name'  :   forms.TextInput(attrs={'class':'form-control'}),
            'student_roll'  :   forms.NumberInput(attrs={'class':'form-control'}),
            'student_email'  :   forms.EmailInput(attrs={'class':'form-control'}),
            'student_gender'  :   forms.Select(attrs={'class':'form-control'}),
            'student_class'  :   forms.Select(attrs={'class':'form-control'}),
            'student_date_of_birth'  :   forms.DateInput(attrs={'class':'form-control'}),
        }

class DeclareResultForm(ModelForm):
    class Meta:
        model = DeclareResult
        fields = ['select_class', 'select_student']
        widgets = {
            'select_class': forms.Select(attrs={'class': 'form-control'}),
            'select_student':  forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'select_class' : 'Class',
            'select_student' : 'Select Student',
        }

class StudentClassForm(ModelForm):
    class Meta:
        model = StudentClass
        exlude  =   'creation_date'
        fields = '__all__'
        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'section':  forms.TextInput(attrs={'class': 'form-control'}),
        }

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'subject_code']
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_code':  forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SubjectCombinationForm(ModelForm):
    class Meta:
        model = SubjectCombination
        fields = ['select_class', 'select_subject']
        widgets = {
            'select_class': forms.Select(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'select_subject':  forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                    }
                ),
        }

