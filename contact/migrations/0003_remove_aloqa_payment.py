# Generated by Django 4.0.3 on 2022-04-17 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_aloqa_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aloqa',
            name='payment',
        ),
    ]