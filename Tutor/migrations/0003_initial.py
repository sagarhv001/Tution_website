# Generated by Django 5.0 on 2024-01-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tutor', '0002_remove_tutor_technology_delete_technology_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('profile_pic', models.FileField(default='default.jpg', upload_to='tutor_pics')),
                ('mobile', models.CharField(max_length=255)),
                ('technology', models.ManyToManyField(to='Tutor.technology')),
            ],
        ),
    ]
