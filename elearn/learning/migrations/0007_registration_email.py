# Generated by Django 4.1 on 2022-09-15 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_remove_registration_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='Email',
            field=models.EmailField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
