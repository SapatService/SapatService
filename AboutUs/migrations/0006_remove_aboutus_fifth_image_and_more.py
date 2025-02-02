# Generated by Django 5.1 on 2024-09-05 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutUs', '0005_rename_image_about_aboutus_first_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='fifth_image',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='first_image',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='fourth_image',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='second_image',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='sixth_image',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='third_image',
        ),
        migrations.CreateModel(
            name='ImageAboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='AbouUsImages/')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AboutUs.aboutus')),
            ],
        ),
    ]
