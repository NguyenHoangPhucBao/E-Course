# Generated by Django 5.0.3 on 2024-03-12 07:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0003_lesson_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]