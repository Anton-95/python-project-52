# Generated by Django 5.1.4 on 2025-02-02 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_label'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='task',
            table='tasks',
        ),
    ]
