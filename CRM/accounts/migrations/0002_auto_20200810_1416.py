# Generated by Django 3.0.5 on 2020-08-10 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='First_Name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Last_Name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='category',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='title',
        ),
    ]