# Generated by Django 4.1.4 on 2023-06-28 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('spc', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=500)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.department')),
            ],
        ),
    ]
