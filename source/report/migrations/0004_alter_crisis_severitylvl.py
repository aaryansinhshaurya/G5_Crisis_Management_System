# Generated by Django 5.1.1 on 2024-12-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_crisis_assignee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crisis',
            name='severitylvl',
            field=models.IntegerField(default=5),
        ),
    ]
