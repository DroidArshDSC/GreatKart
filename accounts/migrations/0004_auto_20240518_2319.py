# Generated by Django 3.1 on 2024-05-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_account_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_active',
        ),
        migrations.AddField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
