# Generated by Django 5.0 on 2024-01-05 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='technology',
        ),
        migrations.DeleteModel(
            name='Technology',
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
    ]