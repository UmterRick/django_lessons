# Generated by Django 4.2.1 on 2023-05-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_lmsuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lmsuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='lmsuser',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
