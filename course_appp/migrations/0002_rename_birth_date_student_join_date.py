# Generated by Django 4.2.5 on 2023-09-30 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_appp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='birth_date',
            new_name='join_date',
        ),
    ]
