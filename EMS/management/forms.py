from django import forms
from .models import (RatingModule, DepartmentModule,
                    RoleModule, AppraisalModule, EmpoyeeModule)


class RatingAddForm(forms.ModelForm):

    class Meta:
        model = RatingModule
        fields = '__all__'
        exclude = ['created_by', 'modified_by']


class DepartmentAddForm(forms.ModelForm):

    class Meta:
        model = DepartmentModule
        fields = '__all__'
        exclude = ['created_by', 'modified_by', 'status']


class RoleAddForm(forms.ModelForm):

    class Meta:
        model = RoleModule
        fields = '__all__'
        exclude = ['created_by', 'modified_by']


class AppraisalAddForm(forms.ModelForm):

    class Meta:
        model = AppraisalModule
        fields = '__all__'
        exclude = ['created_by', 'modified_by']


class EmployeeAddForm(forms.ModelForm):
    login_user_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    department = forms.ModelChoiceField(
        queryset=DepartmentModule.objects.filter(status=0)
    )

    class Meta:
        model = EmpoyeeModule
        fields = ['login_user_name', 'password', 'first_name', 'last_name', 'employee_id',
                'department', 'category', 'date_of_birth', 'date_of_join', 'address', 'phone_no']
        exclude = ['user_name', 'created_by', 'modified_by']


class EmployeeEditForm(forms.ModelForm):
    department = forms.ModelChoiceField(
        queryset=DepartmentModule.objects.filter(status=0)
    )
    class Meta:
        model = EmpoyeeModule
        fields = '__all__'
        exclude = ['user_name', 'password', 'user_name', 'created_by', 'modified_by']