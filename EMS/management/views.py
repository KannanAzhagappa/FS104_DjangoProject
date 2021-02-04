from django.shortcuts import render
import datetime
from django.urls import reverse
from django.views.generic.list import ListView
from .models import RatingModule, DepartmentModule, RoleModule, AppraisalModule, EmpoyeeModule
from .tables import RatingTable, DepartmentTable, RoleTable, AppraisalTable, EmployeeTable
from .forms import RatingAddForm, DepartmentAddForm, RoleAddForm, AppraisalAddForm, EmployeeAddForm, EmployeeEditForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from django.contrib.auth import logout
# Create your views here.


class AuditableMixin:

    def form_valid(self, form, ):
        try:
            if not form.instance.created_by_id:
                form.instance.created_by_id = self.request.user.id
                form.instance.created_on = datetime.datetime.now()
        except:
            form.instance.created_by_id = self.request.user.id
            form.instance.created_on = datetime.datetime.now()
        form.instance.modified_by = self.request.user
        return super().form_valid(form)


class RatingListView(PermissionRequiredMixin, ListView):
    permission_required = ('management.view_ratingmodule')
    raise_exception = True
    template_name = 'management/generic_list_form.html'
    model = RatingModule

    def get_queryset(self, **kwargs):
        return RatingModule.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = RatingTable(self.get_queryset(**kwargs))
        context['title'] = 'List Rating'
        context['btn_title'] = 'Add Rating'
        context['add_url'] = 'management:add_rating'
        context['add_obj_perm'] = 'management.add_ratingmodule'
        return context


class RatingAddView(PermissionRequiredMixin, AuditableMixin, CreateView):
    permission_required = ('management.add_ratingmodule')
    raise_exception = True
    template_name = 'management/generic_add_form.html'
    form_class = RatingAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Rating'
        context['back_url'] = 'management:list_rating'
        return context

    def get_success_url(self, **kwargs):
        return reverse('management:list_rating')


class RatingEditView(PermissionRequiredMixin, AuditableMixin, UpdateView):
    permission_required = ('management.change_ratingmodule')
    raise_exception = True
    template_name = 'management/generic_add_form.html'
    form_class = RatingAddForm
    model = RatingModule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Rating'
        context['back_url'] = 'management:list_rating'
        return context

    def get_success_url(self, **kwargs):
        return reverse('management:list_rating')


class DepartmentListView(PermissionRequiredMixin, ListView):
    permission_required = ('management.view_departmentmodule')
    raise_exception = True
    template_name = 'management/generic_list_form.html'
    model = DepartmentModule

    def get_queryset(self, **kwargs):
        return DepartmentModule.objects.filter(status=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = DepartmentTable(self.get_queryset(**kwargs))
        context['title'] = 'List Department'
        context['btn_title'] = 'Add Department'
        context['add_url'] = 'management:add_department'
        context['add_obj_perm'] = 'management.add_departmentmodule'
        return context


class DepartmentAddView(PermissionRequiredMixin, AuditableMixin, CreateView):
    permission_required = ('management.add_departmentmodule')
    raise_exception = True
    template_name = 'management/generic_add_form.html'
    form_class = DepartmentAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Department'
        context['back_url'] = 'management:list_department'
        return context

    def get_success_url(self, **kwargs):
        return reverse('management:list_department')


class DepartmentEditView(PermissionRequiredMixin, AuditableMixin, UpdateView):
    permission_required = ('management.change_departmentmodule')
    raise_exception = True
    template_name = 'management/generic_add_form.html'
    form_class = DepartmentAddForm
    model = DepartmentModule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Department'
        context['back_url'] = 'management:list_department'
        return context

    def get_success_url(self, **kwargs):
        return reverse('management:list_department')

    
class RoleListView(PermissionRequiredMixin, ListView):
    permission_required = ('management.view_rolemodule')
    raise_exception = True
    template_name = 'management/generic_list_form.html'
    model = RoleModule

    def get_queryset(self, **kwargs):
        return RoleModule.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = RoleTable(self.get_queryset(**kwargs))
        context['title'] = 'List Role'
        context['btn_title'] = 'Add Role'
        context['add_url'] = 'management:add_role'
        context['add_obj_perm'] = 'management.add_rolemodule'
        return context


class RoleAddView(PermissionRequiredMixin, AuditableMixin, CreateView):
    permission_required = ('management.add_rolemodule')
    raise_exception = True
    template_name = 'management/generic_add_form.html'
    form_class = RoleAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Role'
        context['back_url'] = 'management:list_role'
        return context

    def get_success_url(self, **kwargs):
        return reverse('management:list_role')


class RoleEditView(PermissionRequiredMixin, AuditableMixin, UpdateView):
    permission_required = ('management.change_rolemodule')
    raise_exception = True
    template_name = 'management/generic_add_form.html'
    form_class = RoleAddForm
    model = RoleModule
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Role'
        context['back_url'] = 'management:list_role'
        return context

    def get_success_url(self, **kwargs):
        return reverse('management:list_role')

    
class AppraisalListView(PermissionRequiredMixin, ListView):
    permission_required = ('management.view_appraisalmodule')
    raise_exception = True
    template_name = 'management/generic_list_form.html'
    model = AppraisalModule

    def get_queryset(self, **kwargs):
        emp = EmpoyeeModule.objects.get(user_name=self.request.user)
        #import ipdb; ipdb.set_trace()
        if emp.user_name.is_superuser:
            appraisal_obj = AppraisalModule.objects.all()
        elif emp.category.id == 1:
            appraisal_obj = emp.manage_employee.all()
            appraisal_obj = AppraisalModule.objects.filter(employee__in=appraisal_obj)
        else:
            appraisal_obj = AppraisalModule.objects.filter(employee=emp)
        return appraisal_obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = AppraisalTable(self.get_queryset(**kwargs))
        context['title'] = 'List Appraisal'
        context['btn_title'] = 'Add Appraisal'
        context['add_url'] = 'management:add_appraisal'
        context['add_obj_perm'] = 'management.add_appraisalmodule'
        return context


class AppraisalAddView(PermissionRequiredMixin, AuditableMixin, CreateView):
    permission_required = ('management.add_appraisalmodule')
    raise_exception = True
    template_name = 'management/generic_add_form.html'
    form_class = AppraisalAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Appraisal'
        context['back_url'] = 'management:list_appraisal'
        return context

    def get_success_url(self, **kwargs):
        return reverse('management:list_appraisal')


class AppraisalEditView(PermissionRequiredMixin, AuditableMixin, UpdateView):
    permission_required = ('management.change_appraisalmodule')
    raise_exception = True
    template_name = 'management/generic_add_form.html'
    form_class = AppraisalAddForm
    model = AppraisalModule
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Appraisal'
        context['back_url'] = 'management:list_appraisal'
        return context

    def get_success_url(self, **kwargs):
        return reverse('management:list_appraisal')


class EmployeeListView(PermissionRequiredMixin, ListView):
    permission_required = ('management.view_empoyeemodule')
    raise_exception = True
    template_name = 'management/generic_list_form.html'
    model = EmpoyeeModule

    def get_queryset(self, **kwargs):
        
        emp = EmpoyeeModule.objects.get(user_name=self.request.user)
        #import ipdb; ipdb.set_trace()
        if emp.user_name.is_superuser:
            employee_obj = EmpoyeeModule.objects.filter(status=0)
        elif emp.category.id == 1:
            employee_obj = emp.manage_employee.filter(status=0) 
        else:
            employee_obj = EmpoyeeModule.objects.filter(user_name=self.request.user).filter(status=0)
        return employee_obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = EmployeeTable(self.get_queryset(**kwargs))
        context['title'] = 'List Employee'
        context['btn_title'] = 'Add Employee'
        context['add_url'] = 'management:add_employee'
        context['add_obj_perm'] = 'management.add_empoyeemodule'
        return context

    
class EmployeeAddView(PermissionRequiredMixin, AuditableMixin, CreateView):
    permission_required = ('management.add_empoyeemodule')
    raise_exception = True
    template_name = 'management/generic_add_form.html'
    form_class = EmployeeAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Employee'
        context['back_url'] = 'management:list_employee'
        return context

    def form_valid(self, form):
        username = form.cleaned_data.get('login_user_name')
        password = form.cleaned_data.get('password')
        category = form.cleaned_data.get('category')
        group = Group.objects.get(name="manager_role") if (category.id == 1) else Group.objects.get(name="employee_role")
        user = User.objects.create_user(username=username, password=password)
        user.groups.add(group)
        user.save()
        form.instance.user_name = user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('management:list_employee')


class EmployeeEditView(PermissionRequiredMixin, AuditableMixin, UpdateView):
    permission_required = ('management.change_empoyeemodule')
    raise_exception = True
    template_name = 'management/generic_add_form.html'
    form_class = EmployeeEditForm
    model = EmpoyeeModule
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Employee'
        context['back_url'] = 'management:list_employee'
        return context

    def get_success_url(self, **kwargs):
        return reverse('management:list_employee')


class EmployeeDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('management.view_empoyeemodule')
    raise_exception = True
    template_name = 'management/employee_detail_form.html'
    model = EmpoyeeModule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Employee Detail'
        return context


def delete_employee(request, pk):
    employee_obj = EmpoyeeModule.objects.get(pk=pk)
    context = {}
    context['title'] = 'Delete Employee'
    context['back_url'] = 'management:list_employee'
    context['message'] = 'Are you want to Delete Employee?'
    context['name'] = "{} {}".format(employee_obj.first_name, employee_obj.last_name)

    if request.method == 'POST':
        employee_obj.status = 1
        employee_obj.save()
        return HttpResponseRedirect(reverse('management:list_employee'))
    return render(request, 'management/generic_delete_form.html', context)


def delete_department(request, pk):
    department_obj = DepartmentModule.objects.get(pk=pk)
    context = {}
    context['title'] = 'Delete Department'
    context['back_url'] = 'management:list_department'
    context['message'] = 'Are you want to Delete Department?'
    context['name'] = "{}".format(department_obj.department_name)

    if request.method == 'POST':
        department_obj.status = 1
        department_obj.save()
        return HttpResponseRedirect(reverse('management:list_department'))
    return render(request, 'management/generic_delete_form.html', context)


def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))