# Generated by Django 4.0.3 on 2022-04-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_description_hometitle2_description1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title1', models.TextField(max_length=300)),
                ('title1', models.TextField(max_length=300)),
                ('image1', models.ImageField(upload_to='Featured/')),
                ('button1', models.CharField(max_length=300)),
                ('button_link1', models.CharField(max_length=1000)),
                ('sub_title2', models.TextField(max_length=300)),
                ('title2', models.TextField(max_length=300)),
                ('image2', models.ImageField(upload_to='Featured/')),
                ('button2', models.CharField(max_length=300)),
                ('button_link2', models.CharField(max_length=1000)),
                ('sub_title3', models.TextField(max_length=300)),
                ('title3', models.TextField(max_length=300)),
                ('image3', models.ImageField(upload_to='Featured/')),
                ('button3', models.CharField(max_length=300)),
                ('button_link3', models.CharField(max_length=1000)),
                ('sub_title4', models.TextField(max_length=300)),
                ('title4', models.TextField(max_length=300)),
                ('image4', models.ImageField(upload_to='Featured/')),
                ('button4', models.CharField(max_length=300)),
                ('button_link4', models.CharField(max_length=1000)),
            ],
        ),
    ]
