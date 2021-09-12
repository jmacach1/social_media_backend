# Generated by Django 3.2.5 on 2021-09-04 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0018_alter_iseeyauser_django_auth_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iseeyauser',
            name='django_auth_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
