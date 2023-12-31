# Generated by Django 4.1.4 on 2023-07-03 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('p_email', models.CharField(max_length=20)),
                ('p_phone', models.CharField(max_length=30)),
                ('booking_date', models.DateField()),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctors')),
            ],
        ),
    ]
