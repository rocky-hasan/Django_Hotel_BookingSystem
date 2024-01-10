# Generated by Django 5.0.1 on 2024-01-09 20:24

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('9cd329b4-a46b-472e-85c6-3b47c409492a'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('amenity_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('9cd329b4-a46b-472e-85c6-3b47c409492a'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('hotel_name', models.CharField(max_length=180)),
                ('hotel_price', models.IntegerField()),
                ('description', models.TextField()),
                ('room_count', models.IntegerField(default=10)),
                ('amenities', models.ManyToManyField(to='app.amenities')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hotel_Booking',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('9cd329b4-a46b-472e-85c6-3b47c409492a'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('start_at', models.DateField()),
                ('end_at', models.DateField()),
                ('booking_type', models.CharField(choices=[('Pre Book', 'Pre Book'), ('Post Book', 'Post Book')], max_length=180)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_booking', to='app.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hotel_Images',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('9cd329b4-a46b-472e-85c6-3b47c409492a'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='hotel/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_images', to='app.hotel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]