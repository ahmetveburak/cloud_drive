# Generated by Django 3.2.6 on 2021-09-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0003_alter_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=32, unique=True, verbose_name='Token'),
        ),
    ]
