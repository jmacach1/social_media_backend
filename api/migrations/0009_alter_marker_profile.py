# Generated by Django 3.2.5 on 2021-08-28 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210828_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.profile'),
        ),
    ]
