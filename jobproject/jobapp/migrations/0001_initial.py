# Generated by Django 4.2 on 2024-04-22 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobs_data',
            fields=[
                ('job_Id', models.AutoField(primary_key=True, serialize=False)),
                ('job_Name', models.CharField(max_length=100)),
                ('job_Company', models.CharField(max_length=100)),
                ('job_Location', models.CharField(max_length=100)),
                ('job_Desc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
    ]
