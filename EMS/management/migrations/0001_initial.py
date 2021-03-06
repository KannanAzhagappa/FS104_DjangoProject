# Generated by Django 3.1.4 on 2021-02-02 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('department_name', models.CharField(max_length=100, verbose_name='Department Name')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departmentmodule_Created_By', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departmentmodule_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoleModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('role_name', models.CharField(max_length=100, verbose_name='Role Name')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rolemodule_Created_By', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rolemodule_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RatingModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('rating_name', models.CharField(max_length=100, verbose_name='Rating Number')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratingmodule_Created_By', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratingmodule_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmpoyeeModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('date_of_birth', models.DateField()),
                ('date_of_join', models.DateField()),
                ('employee_id', models.IntegerField(verbose_name='Employee Number')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('phone_no', models.CharField(max_length=100, verbose_name='Phone Number')),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'InActive')], default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.rolemodule', verbose_name='Category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empoyeemodule_Created_By', to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.departmentmodule', verbose_name='DepartMent')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empoyeemodule_modified_by', to=settings.AUTH_USER_MODEL)),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AppraisalModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('year', models.IntegerField(verbose_name='Year')),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_appraisal', to='management.empoyeemodule', verbose_name='Employee')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appraisalmodule_Created_By', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_appraisal', to='management.empoyeemodule', verbose_name='Employee')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appraisalmodule_modified_by', to=settings.AUTH_USER_MODEL)),
                ('rating', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.ratingmodule', verbose_name='Rating')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
