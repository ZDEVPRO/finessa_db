# Generated by Django 4.0.3 on 2022-04-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_hometitle1_content_hometitle1_description1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hometitle2',
            old_name='description',
            new_name='description1',
        ),
        migrations.RemoveField(
            model_name='hometitle2',
            name='title',
        ),
        migrations.AddField(
            model_name='hometitle2',
            name='description2',
            field=models.TextField(default='desc1', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hometitle2',
            name='title1',
            field=models.CharField(default='desc2', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hometitle2',
            name='title2',
            field=models.CharField(default='title', max_length=300),
            preserve_default=False,
        ),
    ]
