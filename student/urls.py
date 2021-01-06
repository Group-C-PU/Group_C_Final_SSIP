from django.urls import path
from student.controllers.dashboard_controller import DashboardView,registerPage,PasswordChangeView
from student.controllers.result_controller import declare_result_view,result_update_view,result_delete_view,DeclareResultListView,validate_data,setup_update_view
from student.controllers.class_controller import StudentClassCreateView,StudentClassUpdateView,StudentClassDeleteView,StudentClassListView
from student.controllers.student_controller import StudentListView,StudentCreateView,StudentUpdateView,StudentDeleteView, searchStudents
from student.controllers.subject_controller import SubjectListView,SubjectCreateView,SubjectUpdateView,SubjectDeleteView
from student.controllers.com_subj_class_controller import SubjectCombinationListView,SubjectCombinationDeleteView,SubjectCombinationUpdateView,SubjectCombinationCreateView
from student.controllers.ID_controller import IDCreateView,IDDeleteView,IDListView,IDUpdateView
from student.controllers.calender_controller import calender_Holiday

urlpatterns = [
    path('',DashboardView.as_view(), name='dashboard'),
    path('register/',registerPage, name='register'),
    path('change-password/', PasswordChangeView.as_view(), name='change_password'),
    path('declare/',declare_result_view, name='declare_result'),
    path('result/update/<int:pk>/', result_update_view, name='update_result'),
    path('result/delete/<int:pk>/', result_delete_view, name='delete_result'),
    path('result/list/', DeclareResultListView.as_view(), name='result_list'),
    path('declare/validate/', validate_data, name='validate_data'),
    path('declare/setup/', setup_update_view, name='setup'),
    path('class/create/', StudentClassCreateView.as_view(), name='create_class'),
    path('class/update/<int:pk>/', StudentClassUpdateView.as_view(), name='update_class'),
    path('class/delete/<int:pk>/', StudentClassDeleteView.as_view(), name='delete_class'),
    path('class/list/', StudentClassListView.as_view(), name='class_list'),
    path('student/', StudentListView.as_view(), name='student_list'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name='student_update'),
    path('student/delete/<int:pk>', StudentDeleteView.as_view(), name='student_delete'),
    path('subject/', SubjectListView.as_view(), name='subject_list'),
    path('subject/create/', SubjectCreateView.as_view(), name='create_subject'),
    path('subject/update/<int:pk>/', SubjectUpdateView.as_view(), name='update_subject'),
    path('subject/delete/<int:pk>/', SubjectDeleteView.as_view(), name='delete_subject'),
    path('combination/create/', SubjectCombinationCreateView.as_view(), name='create_subject_combination' ),
    path('combination/list/', SubjectCombinationListView.as_view(), name='subject_combination_list' ),
    path('combination/update/<int:pk>', SubjectCombinationUpdateView.as_view(), name='subject_combination_update' ),
    path('combination/delete/<int:pk>', SubjectCombinationDeleteView.as_view(), name='subject_combination_delete' ),
    path('student/id/', IDListView.as_view(), name='id_list'),
    path('student/id/create/', IDCreateView.as_view(), name='id_create'),
    path('student/id/update/<int:pk>',IDUpdateView.as_view(), name='id_update'),
    path('student/id/delete/<int:pk>', IDDeleteView.as_view(), name='id_delete'),
    path('calendar/', calender_Holiday, name='calendar'),
    path('search/',searchStudents,name='search_students'),
]