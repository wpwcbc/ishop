# Generated by Django 2.0.7 on 2018-09-06 02:55

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
            name='Item',
            fields=[
                ('IID', models.AutoField(primary_key=True, serialize=False)),
                ('Price', models.DecimalField(decimal_places=1, max_digits=7)),
                ('Type', models.CharField(choices=[('Textbook', 'Textbook'), ('Instrument', 'Instrument'), ('SchoolUniform', 'SchoolUniform'), ('Stationary', 'Stationary'), ('Others', 'Others')], max_length=13)),
                ('LaunchDate', models.DateField(auto_now_add=True)),
                ('TradingLocation', models.CharField(max_length=50)),
                ('Status', models.BooleanField(default=False)),
                ('Name', models.CharField(max_length=30)),
                ('Description', models.TextField(max_length=30)),
                ('Seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('PID', models.AutoField(primary_key=True, serialize=False)),
                ('ContactNo', models.CharField(max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]