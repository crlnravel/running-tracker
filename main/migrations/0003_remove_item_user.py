# Generated by Django 5.0.2 on 2024-02-27 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]
