# Generated by Django 3.2.1 on 2024-07-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0019_booking_guests'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='table_img',
            field=models.ImageField(blank=True, upload_to='cover/'),
        ),
    ]