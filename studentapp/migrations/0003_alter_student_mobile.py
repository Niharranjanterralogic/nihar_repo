# Generated by Django 4.0.5 on 2022-06-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_remove_student_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]