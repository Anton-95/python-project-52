# Generated by Django 5.1.4 on 2025-01-21 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_options_alter_users_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='users',
            name='updated_at',
        ),
    ]
