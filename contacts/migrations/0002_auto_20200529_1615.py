# Generated by Django 3.0.5 on 2020-05-29 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='name',
            new_name='contact',
        ),
    ]
