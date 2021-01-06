from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from io import BytesIO
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from student.models.result import DeclareResult
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.core import serializers
import json

from django.contrib import messages
from student.forms import CreateUserForm
from student.models.Class import StudentClass
from student.models.subject import Subject
from student.models.student import Student


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("\nUser Name = ",username)
        print("Password = ",password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            context = {'message':'Invalid User Name and Password'}
            return render(request, 'dashboard/index.html', context)
    return render(request, 'dashboard/index.html', {})

def registerPage(request):
    form = CreateUserForm()
    if request.method =='POST':
        email = request.POST['email']
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            template = render_to_string('dashboard/email.html',{'username':request.user.username})
            sent = render_to_string('dashboard/send.html')
            email = EmailMessage(
                'Account - E-Mail validation',
                template,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email.fail_silently = False
            email.send()
            return HttpResponse(sent)
    context = {'form':form}
    return render(request, 'dashboard/register.html', context)



class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard/dashboard.html"

    
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['cls'] = StudentClass.objects.count()
        context['results'] = DeclareResult.objects.count()
        context['students'] = Student.objects.count()
        context['subjects'] = Subject.objects.count()
        return context

class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('dashboard:dashboard')
    template_name = 'dashboard/password_change_form.html'

    
    def get_context_data(self, **kwargs):
        context = super(PasswordChangeView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Admin Change Password'
        context['panel_title'] = 'Admin Change Password'
        return context


def renderPdf(template, content={}):
    t = get_template(template)
    send_data = t.render(content)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(send_data.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return None

class pdf(View):
    def get(self, request, id):
        try:
            query = get_object_or_404(DeclareResult, id=id)
        except:
            Http404('Content Not Found')
        marks = []
        lst = []
        for i in range(int(len(query.marks)/2)):
            lst.append(query.marks['subject_'+str(i)])
            lst.append(query.marks['subject_'+str(i)+'_mark'])
            marks.append(lst)
            lst = []
        article_pdf = renderPdf('dashboard/result.html', {'object': query, 'marks':marks})
        return HttpResponse(article_pdf, content_type='application/pdf')
