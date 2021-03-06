# Generated by Django 4.0.5 on 2022-06-14 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='landing_page',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pics'),
        ),
    ]
