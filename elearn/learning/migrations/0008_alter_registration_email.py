# Generated by Django 4.1 on 2022-09-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_registration_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='Email',
            field=models.EmailField(default='', max_length=200),
        ),
    ]