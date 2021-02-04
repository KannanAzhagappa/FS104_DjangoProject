from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import RatingListView, RatingAddView, RatingEditView
from .views import DepartmentListView, DepartmentAddView, DepartmentEditView
from .views import RoleListView, RoleAddView, RoleEditView
from .views import AppraisalListView, AppraisalAddView, AppraisalEditView
from .views import (EmployeeListView, EmployeeAddView, EmployeeEditView, EmployeeDetailView,
delete_employee, userlogout, delete_department)

app_name = 'management'

urlpatterns = [
    path('list_rating', login_required(RatingListView.as_view()), name='list_rating'),
    path('add_rating', login_required(RatingAddView.as_view()), name='add_rating'),
    path('edit_rating/<int:pk>/', login_required(RatingEditView.as_view()), name='edit_rating'),

    path('list_department', login_required(DepartmentListView.as_view()), name='list_department'),
    path('add_department', login_required(DepartmentAddView.as_view()), name='add_department'),
    path('edit_department/<int:pk>/', login_required(DepartmentEditView.as_view()), name='edit_department'),
    path('delete_department/<int:pk>/', login_required(delete_department), name='delete_department'),

    path('list_role', login_required(RoleListView.as_view()), name='list_role'),
    path('add_role', login_required(RoleAddView.as_view()), name='add_role'),
    path('edit_role/<int:pk>/', login_required(RoleEditView.as_view()), name='edit_role'),

    path('list_appraisal', login_required(AppraisalListView.as_view()), name='list_appraisal'),
    path('add_appraisal', login_required(AppraisalAddView.as_view()), name='add_appraisal'),
    path('edit_appraisal/<int:pk>/', login_required(AppraisalEditView.as_view()), name='edit_appraisal'),

    path('list_employee', login_required(EmployeeListView.as_view()), name='list_employee'),
    path('detail_employee/<int:pk>/', login_required(EmployeeDetailView.as_view()), name='detail_employee'),
    path('add_employee', login_required(EmployeeAddView.as_view()), name='add_employee'),
    path('edit_employee/<int:pk>/', login_required(EmployeeEditView.as_view()), name='edit_employee'),
    path('delete_employee/<int:pk>/', login_required(delete_employee), name='delete_employee'),

    path('logout', userlogout, name='logout'),
]
