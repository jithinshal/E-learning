# Generated by Django 4.1 on 2022-09-12 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_rename_course_chapter_content_name_learning_progress_course_chapter_content_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='Chapter_text_Content',
            new_name='Chapter_text_content',
        ),
    ]
