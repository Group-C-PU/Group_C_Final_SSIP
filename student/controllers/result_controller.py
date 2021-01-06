from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from student.models.result import DeclareResult
from student.forms import DeclareResultForm
from student.models.Com_subj_class import SubjectCombination
from student.models.Class import StudentClass
from student.models.student import Student
from django.http import HttpResponse, JsonResponse

from django.core import serializers
import json


def validate_data(request):
    smt = SubjectCombination.objects.all()
    data = {}
    if request.method == "GET":
        rc = request.GET['selectedClass']
        subjects = []
        for s in smt:
            if s.select_class.class_name in rc and s.select_class.section in rc:
                subjects.append(s.select_subject)
        sir_subjects = serializers.serialize('json', subjects)
        data['subjects'] = sir_subjects
        return JsonResponse(data)
    subjects = None
    data['result'] = 'you made a request with empty data'
    return HttpResponse(json.dumps(data), content_type="application/json")

def declare_result_view(request):
    context = {}

    if request.method == "POST":
        form = request.POST
        data = json.loads(json.dumps(form))
        data.pop('csrfmiddlewaretoken')
        pk = data['select_class']
        clas = StudentClass.objects.get(id=pk)
        pk = data['select_student']
        student = Student.objects.get(id=pk)
        data.pop('select_class')
        data.pop('select_student')
        DeclareResult.objects.create(select_class=clas, select_student=student, marks=data)
    else:
        form = DeclareResultForm()
        context['main_page_title'] = 'Declare Students Result'
        context['panel_name'] = 'Results'
        context['panel_title'] = 'Declare Result'
        context['form'] = form
    return render(request, "result/declareresult_form.html", context)

def setup_update_view(request):
    data = {}
    if request.method == "GET":
        pk_value = int(request.GET['pk_value'])
        result_obj = get_object_or_404(DeclareResult, pk = pk_value)
        dt = result_obj.marks
        data['dt'] = dt
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(json.dumps(data), content_type="application/json")

@login_required
def result_update_view(request, pk):
    result = get_object_or_404(DeclareResult, pk=pk)
    form = DeclareResultForm(instance=result)
    context = {}
    context['main_page_title'] = 'Update Students Result'
    context['panel_name'] = 'Results'
    context['panel_title'] = 'Update Result'
    context['form'] = form
    context['pk'] = pk
    if request.method == "POST":
        all_data = request.POST
        data = json.loads(json.dumps(all_data))
        data.pop('csrfmiddlewaretoken')
        pk = data['select_class']
        clas = StudentClass.objects.get(id=pk)
        pk = data['select_student']
        student = Student.objects.get(id=pk)
        data.pop('select_class')
        data.pop('select_student')
        print('Modified Data = ', data)
        result.select_class = clas
        result.select_student = student
        result.marks = data
        result.save()
        print('\nResult updated\n')
        return redirect('result_list')
    return render(request, "result/update_form.html", context)

@login_required
def result_delete_view(request, pk):
    obj = get_object_or_404(DeclareResult, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('result_list')
    return render(request, "result/result_delete.html", {"object":obj})

class DeclareResultListView(LoginRequiredMixin, ListView):
    model = DeclareResult
    template_name='result/declareresult_list.html'
    field_list = [
        'Student Name', 'Roll No', 'Class', 'Reg Date', 'View Result'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Results'
        context['panel_name']   =   'Results'
        context['panel_title']  =   'View Results Info'
        context['field_list']   =   self.field_list
        return context
    
