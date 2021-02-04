from django.contrib import admin
from .models import (AppraisalModule, DepartmentModule,
EmpoyeeModule, RatingModule, RoleModule)
# Register your models here.


@admin.register(AppraisalModule)
class AppraisalModuleAdmin(admin.ModelAdmin):
    search_fields = ('employee', 'year', 'approved_by', 'rating')
    list_display = ('employee', 'year')


@admin.register(DepartmentModule)
class DepartmentModuleAdmin(admin.ModelAdmin):
    search_fields = ('department_name', 'description')
    list_display = ('department_name', 'description')


@admin.register(RatingModule)
class RatingModuleAdmin(admin.ModelAdmin):
    search_fields = ('rating_name', 'description')
    list_display = ('rating_name', 'description')


@admin.register(RoleModule)
class RoleModuleAdmin(admin.ModelAdmin):
    search_fields = ('role_name', 'description')
    list_display = ('role_name', 'description')


@admin.register(EmpoyeeModule)
class EmpoyeeModuleAdmin(admin.ModelAdmin):
    search_fields = ('user_name', 'category', 'first_name', 'last_name')
    list_display = ('user_name', 'category', 'first_name', 'last_name')
