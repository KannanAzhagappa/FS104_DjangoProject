# Generated by Django 3.1.6 on 2021-02-03 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_empoyeemodule_manage_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empoyeemodule',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.departmentmodule', verbose_name='Department'),
        ),
    ]
