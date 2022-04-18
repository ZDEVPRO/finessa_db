# Generated by Django 4.0.3 on 2022-04-07 07:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_hometitle2_rename_hometitle_hometitle1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hometitle1',
            name='description',
        ),
        migrations.RemoveField(
            model_name='hometitle1',
            name='title',
        ),
        migrations.AddField(
            model_name='hometitle1',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='cpn'),
            preserve_default=False,
        ),
    ]
