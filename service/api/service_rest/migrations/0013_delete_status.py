# Generated by Django 4.0.3 on 2023-04-27 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0012_alter_status_options_alter_appointment_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]