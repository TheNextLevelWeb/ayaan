# Generated by Django 4.2.3 on 2024-05-18 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_users_feedback_alter_users_username_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='ser',
            new_name='username',
        ),
    ]
