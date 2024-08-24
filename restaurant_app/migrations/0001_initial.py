# Generated by Django 3.2.1 on 2024-06-15 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True, verbose_name='Enquiry')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pictures/')),
                ('contact', models.CharField(blank=True, max_length=500)),
                ('selected_choice', models.CharField(blank=True, max_length=500)),
                ('selected_plan_paid', models.BooleanField(default=False)),
                ('bookings', models.ManyToManyField(blank=True, related_name='_restaurant_app_profile_bookings_+', to='restaurant_app.Profile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
