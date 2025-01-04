# Generated by Django 5.0.6 on 2024-11-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='COMEDK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('registration_number', models.CharField(max_length=20)),
                ('taken_comedk', models.BooleanField(default=False)),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('campus', models.CharField(blank=True, max_length=100, null=True)),
                ('comedk_rank', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('comedk_registration_number', models.CharField(blank=True, max_length=20, null=True)),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
