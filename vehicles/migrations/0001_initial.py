# Generated by Django 4.0.6 on 2022-08-11 07:21

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=150, unique=True)),
                ('year', models.PositiveIntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)])),
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=20)),
                ('description', ckeditor.fields.RichTextField()),
                ('horse_power', models.PositiveIntegerField(blank=True)),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=20)),
                ('doors', models.CharField(choices=[('2', '2'), ('4', '4')], max_length=10)),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Kerosine', 'Kerosine'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=20)),
                ('drive', models.CharField(choices=[('2x2 Drive', '2x2 Drive'), ('4x4 Drive', '4x4 Drive')], max_length=15)),
                ('car_photo', models.ImageField(upload_to='cars_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('car_photo_1', models.ImageField(blank=True, null=True, upload_to='cars_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('car_photo_2', models.ImageField(blank=True, null=True, upload_to='cars_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('car_photo_3', models.ImageField(blank=True, null=True, upload_to='cars_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('features', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Audio Input', 'Audio Input'), ('Air Conditioning', 'Air Conditioning'), ('Heated seats', 'Heated seats'), ('Alarm System', 'Alarm System'), ('Bluetooth', 'Bluetooth'), ('GPS Navigation', 'GPS Navigation'), ('Parking Sensors', 'Parking Sensors'), ('Rear View Camera', 'Rear View Camera'), ('USB input', 'USB input'), ('FM Radio', 'FM Radio'), ('Remote central locking', 'Remote central locking'), ('Child Seat', 'Child Seat'), ('Wifi Access', 'Wifi Access')], max_length=177)),
                ('seats', models.PositiveIntegerField()),
                ('vin_no', models.CharField(max_length=17)),
                ('mileage', models.PositiveIntegerField(blank=True)),
                ('is_booked', models.BooleanField(blank=True, default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pick_up_date', models.DateTimeField()),
                ('drop_off_date', models.DateTimeField()),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(blank=True, default=False)),
                ('vehicle_returned', models.BooleanField(blank=True, default=False)),
                ('is_completed', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='vehicles.vehicle')),
            ],
            options={
                'ordering': ['-booking_date'],
            },
        ),
    ]
