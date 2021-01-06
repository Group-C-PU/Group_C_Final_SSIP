from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from student.models.Com_subj_class import SubjectCombination
from student.forms import SubjectCombinationForm
from django.urls import reverse_lazy

class SubjectCombinationCreateView(LoginRequiredMixin, CreateView):
    model = SubjectCombination
    form_class = SubjectCombinationForm
    template_name = 'com_subj_class/subjectcombination_form.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectCombinationCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'SubjectCombination Creation'
        context['panel_name'] = 'SubjectConbinations'
        context['panel_title'] = 'Create SubjectConbination'
        return context

class SubjectCombinationListView(LoginRequiredMixin, ListView):
    model = SubjectCombination
    template_name = 'com_subj_class/subjectcombination_list.html'
    field_list = [
        'Class', 'Section', 'Subject'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage SubjectCombinations'
        context['panel_name']   =   'SubjectCombinations'
        context['panel_title']  =   'View SubjectCombinations Info'
        context['field_list']   =   self.field_list
        return context

class SubjectCombinationUpdateView(LoginRequiredMixin, UpdateView):
    model = SubjectCombination
    template_name = 'com_subj_class/subjectcombination_form.html'
    form_class = SubjectCombinationForm
    success_url = reverse_lazy('subject_combination_list')

class SubjectCombinationDeleteView(LoginRequiredMixin, DeleteView):
    model = SubjectCombination
    template_name = 'com_subj_class/subjectcombination_delete.html'
    success_url = reverse_lazy('subject_combination_list')

    def get_context_data(self, **kwargs):
        context = super(SubjectCombinationDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'SubjectCombination Delete Confirmation'
        context['panel_name'] = 'SubjectCombinations'
        context['panel_title'] = 'Delete SubjectCombination'
        return context
