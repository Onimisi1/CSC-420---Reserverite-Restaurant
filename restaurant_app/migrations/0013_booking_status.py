# Generated by Django 3.2.1 on 2024-06-15 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0012_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant_app.status'),
            preserve_default=False,
        ),
    ]