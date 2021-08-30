# Generated by Django 3.2.6 on 2021-08-30 19:24

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='modified',
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Private'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='File Name'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=martor.models.MartorField(verbose_name='Post Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Private'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Post Title'),
        ),
    ]