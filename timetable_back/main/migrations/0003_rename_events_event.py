# Generated by Django 4.1.7 on 2023-02-25 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_events_desc_events_etime_events_stime'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]