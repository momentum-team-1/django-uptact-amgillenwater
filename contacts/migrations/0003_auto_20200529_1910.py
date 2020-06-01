# Generated by Django 3.0.5 on 2020-05-29 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200529_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='contacts.Contact'),
        ),
    ]
