# Generated by Django 3.2.6 on 2021-09-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='U592nJrt87zYo8OyuFkN0RXyjyGtiJJB', max_length=32, unique=True, verbose_name='Token'),
        ),
    ]
