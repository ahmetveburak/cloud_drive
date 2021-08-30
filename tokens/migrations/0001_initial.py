# Generated by Django 3.2.6 on 2021-08-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='cHg87fkGNbCMxDF9fl12QEx4vKtgu3D5', max_length=32, verbose_name='Token')),
                ('counter', models.SmallIntegerField(default=0)),
                ('enabled_count', models.SmallIntegerField(default=0)),
                ('enabled_to', models.DateTimeField(blank=True, null=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]