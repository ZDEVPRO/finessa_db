# Generated by Django 4.0.3 on 2022-04-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aloqa',
            name='payment',
            field=models.CharField(default='naq pul', max_length=300, verbose_name='To`lov turi'),
            preserve_default=False,
        ),
    ]
