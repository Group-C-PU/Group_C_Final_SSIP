from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from student.models.ID import Student_ID
from student.forms import IDForm
from django.urls import reverse_lazy


class IDCreateView(LoginRequiredMixin, CreateView):
    model = Student_ID
    form_class = IDForm
    template_name='id/id_form.html'
    def get_context_data(self, **kwargs):
        context = super(IDCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Student ID Creation'
        context['panel_name'] = 'Student ID'
        context['panel_title'] = 'Add Student ID'
        return context

class IDListView(LoginRequiredMixin, ListView):
    model = Student_ID
    template_name='id/id_list.html'
    field_list = [
        'Student id'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Student ID'
        context['panel_name']   =   'Student ID'
        context['panel_title']  =   'View Student ID Info'
        context['field_list']   =   self.field_list
        return context

class IDUpdateView(LoginRequiredMixin,UpdateView):
    model = Student_ID
    template_name='id/id_form.html'
    form_class = IDForm
    success_url = reverse_lazy('id_list')

class IDDeleteView(LoginRequiredMixin, DeleteView):
    model = Student_ID
    template_name= 'id/id_delete.html'
    success_url = reverse_lazy('id_list')

    def get_context_data(self, **kwargs):
        context = super(IDDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Student ID Delete Confirmation'
        context['panel_name'] = 'Student ID'
        context['panel_title'] = 'Delete Student ID'
        return context