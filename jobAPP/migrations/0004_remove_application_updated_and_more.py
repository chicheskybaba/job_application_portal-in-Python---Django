# Generated by Django 4.1.3 on 2023-01-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobAPP', '0003_application_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='updated',
        ),
        migrations.AlterField(
            model_name='application',
            name='coverletter',
            field=models.TextField(max_length=1500),
        ),
    ]
