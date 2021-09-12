# Generated by Django 3.2.5 on 2021-08-28 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_marker_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='currentLocation',
        ),
        migrations.AlterField(
            model_name='marker',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location'),
        ),
    ]