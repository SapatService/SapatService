# Generated by Django 5.1 on 2024-09-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0002_alter_geolocate_options_alter_instagram_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteam',
            name='image',
            field=models.ImageField(default=1, upload_to='OurTeamImage/', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
