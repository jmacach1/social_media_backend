# Generated by Django 3.2.5 on 2021-08-27 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_marker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='type',
            field=models.CharField(choices=[('address', 'address'), ('profile', 'profile')], default='address', max_length=30),
        ),
    ]