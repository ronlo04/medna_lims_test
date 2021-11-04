# Generated by Django 3.2.5 on 2021-10-19 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import utility.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('grant_code', models.CharField(max_length=1, unique=True, verbose_name='Grant Code')),
                ('grant_label', models.CharField(max_length=255, verbose_name='Grant Label')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Grant',
                'verbose_name_plural': 'Grants',
            },
        ),
        migrations.CreateModel(
            name='PeriodicTaskRun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255, verbose_name='Task Name')),
                ('task_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('project_code', models.CharField(max_length=255, unique=True, verbose_name='Project Code')),
                ('project_label', models.CharField(max_length=255, verbose_name='Project Label')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('grant_name', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.RESTRICT, to='utility.grant')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProcessLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('process_location_name', models.CharField(max_length=255, unique=True, verbose_name='Location Name')),
                ('process_location_name_slug', models.SlugField(max_length=255, verbose_name='Location Name Slug')),
                ('affiliation', models.CharField(max_length=255, verbose_name='Affiliation')),
                ('process_location_url', models.URLField(max_length=255, verbose_name='Location URL')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone Number')),
                ('location_email_address', models.EmailField(blank=True, max_length=254, verbose_name='Location Email Address')),
                ('point_of_contact_email_address', models.EmailField(blank=True, max_length=254, verbose_name='Point of Contact Email Address')),
                ('point_of_contact_first_name', models.CharField(blank=True, max_length=255, verbose_name='Point of Contact First Name')),
                ('point_of_contact_last_name', models.CharField(blank=True, max_length=255, verbose_name='Point of contact Last Name')),
                ('location_notes', models.TextField(blank=True, verbose_name='Notes')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Process Location',
                'verbose_name_plural': 'Process Locations',
            },
        ),
    ]