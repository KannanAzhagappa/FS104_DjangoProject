from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

STATUS = (
    (0, 'Active'),
    (1, 'InActive')
)


class AuditableModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='%(class)s_Created_By',
        on_delete=models.CASCADE)

    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='%(class)s_modified_by',
        on_delete=models.CASCADE)

    class Meta:
        abstract = True


class RoleModule(AuditableModel):
    role_name = models.CharField(max_length=100, verbose_name='Role Name')
    description = models.TextField('Description', max_length=250, blank=True, null=True)

    def __str__(self):
        return self.role_name


class DepartmentModule(AuditableModel):
    department_name = models.CharField(max_length=100, verbose_name='Department Name')
    description = models.TextField(
        'Description', max_length=250, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.department_name


class EmpoyeeModule(AuditableModel):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'RoleModule', verbose_name='Category', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    date_of_birth = models.DateField()
    date_of_join = models.DateField()
    employee_id = models.IntegerField(verbose_name='Employee Number')
    department = models.ForeignKey(
        'DepartmentModule', verbose_name='Department', blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, verbose_name='Address')
    phone_no = models.CharField(max_length=100, verbose_name='Phone Number')
    manage_employee = models.ManyToManyField('self', blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class RatingModule(AuditableModel):
    rating_name = models.CharField(max_length=100, verbose_name='Rating Number')
    description = models.TextField(
        'Description', max_length=250, blank=True, null=True)

    def __str__(self):
        return self.rating_name


class AppraisalModule(AuditableModel):
    employee = models.ForeignKey(
        'EmpoyeeModule', verbose_name='Employee Name', blank=True, null=True, related_name='employee_appraisal', on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='Year')
    approved_by = models.ForeignKey(
        'EmpoyeeModule', verbose_name='Approved By', blank=True, null=True, related_name='manager_appraisal', on_delete=models.CASCADE)
    rating = models.ForeignKey(
        'RatingModule', verbose_name='Rating', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.employee)
