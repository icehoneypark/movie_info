# Generated by Django 3.2.9 on 2021-11-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='community_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
