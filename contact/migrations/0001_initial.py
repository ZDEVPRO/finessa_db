# Generated by Django 4.0.3 on 2022-04-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aloqa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=100, verbose_name='Familiya')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon')),
                ('product_id', models.CharField(max_length=50, verbose_name='Maxsulot Id raqami')),
                ('message', models.TextField(max_length=1000, verbose_name='Mijoz Manzili va xabari')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Xabar kelgan vaqt')),
                ('ip', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Buyurtmalar',
                'verbose_name_plural': 'Buyurtmalar',
            },
        ),
    ]
