# Generated by Django 3.2.25 on 2024-05-17 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0037_auto_20240425_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banktransactionmodel',
            name='current_amount',
        ),
    ]