# Generated by Django 3.2.6 on 2021-09-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_file_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]