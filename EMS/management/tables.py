import itertools
import django_tables2 as tables
from django_tables2.utils import A
from .models import AppraisalModule, EmpoyeeModule

def table_counter(self):
    page = int(self.request.GET.get('page', 1)) - 1
    self.row_counter = getattr(
        self, 'row_counter', itertools.count(start=page*15+1))
    return next(self.row_counter)


class RatingTable(tables.Table):
    rating_name = tables.Column(verbose_name='Rating Name')
    description = tables.Column(verbose_name='Description')
    edit = tables.TemplateColumn(
        """<a class="btn btn-info btn-sm" href='{%url "management:edit_rating" record.id %}'>Edit</a>""",
        verbose_name='Action', orderable=False)

    def before_render(self, request):
        if not request.user.has_perm('management.change_ratingmodule'):
            self.columns.hide('edit')

    class Meta:
        orderable = True
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ['rating_name', 'description', 'edit']


class DepartmentTable(tables.Table):
    department_name = tables.Column(verbose_name='Department Name')
    description = tables.Column(verbose_name='Description')
    edit = tables.TemplateColumn(
        """<a class="btn btn-info btn-sm" href='{%url "management:edit_department" record.id %}'>Edit</a>
           <a class="btn btn-danger btn-sm" href='{%url "management:delete_department" record.id %}'>Delete</a>
        """, verbose_name='Action', orderable=False)    

    def before_render(self, request):
        if not request.user.has_perm('management.change_departmentmodule'):
            self.columns.hide('edit')

    class Meta:
        orderable = True
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ['department_name', 'description']


class RoleTable(tables.Table):
    role_name = tables.Column(verbose_name='Role Name')
    description = tables.Column(verbose_name='Role Description')
    edit = tables.TemplateColumn(
        """<a class="btn btn-info btn-sm" href='{%url "management:edit_role" record.id %}'>Edit</a>""",
        verbose_name='Action', orderable=False)

    def before_render(self, request):
        if not request.user.has_perm('management.change_rolemodule'):
            self.columns.hide('edit')

    class Meta:
        orderable = True
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ['role_name', 'description']

    
class AppraisalTable(tables.Table):

    edit = tables.TemplateColumn(
        """<a class="btn btn-info btn-sm" href='{%url "management:edit_appraisal" record.id %}'>Edit</a>""",
        verbose_name='Action', orderable=False)

    def before_render(self, request):
        if not request.user.has_perm('management.change_appraisalmodule'):
            self.columns.hide('edit')

    class Meta:
        model = AppraisalModule
        orderable = True
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ['employee', 'year', 'rating', 'approved_by', 'edit']
        

class EmployeeTable(tables.Table):
    employee_id = tables.LinkColumn('management:detail_employee',
                            args=[A('pk')], orderable=False)
    edit = tables.TemplateColumn(
        """<a class="btn btn-info btn-sm" href='{%url "management:edit_employee" record.id %}'>Edit</a>
           <a class="btn btn-danger btn-sm" href='{%url "management:delete_employee" record.id %}'>Delete</a>
        """, verbose_name='Action', orderable=False)    

    def before_render(self, request):
        if not request.user.has_perm('management.change_empoyeemodule'):
            self.columns.hide('edit')

    class Meta:
        model = EmpoyeeModule
        orderable = True
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ['employee_id', 'first_name', 'last_name', 'date_of_join', 'department', 'category', 'edit']