# Generated by Django 3.1 on 2024-05-28 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20240523_0136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='variation',
            new_name='variations',
        ),
    ]
