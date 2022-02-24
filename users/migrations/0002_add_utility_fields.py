# Generated manually on 02-10-2022
from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields
import users.models
import medna_metadata.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='CustomUser',
            name='custom_user_css',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='utility.customusercss', related_name="selected_user_css", verbose_name="Selected Color Profile"),
        ),
        migrations.AddField(
            model_name='CustomUser',
            name='affiliated_projects',
            field=models.ManyToManyField(to='utility.project', related_name="affiliated_projects", verbose_name="Affiliated Project(s)"),
        ),
    ]