# Generated by Django 3.1 on 2024-05-28 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='variations',
            new_name='variation',
        ),
    ]
