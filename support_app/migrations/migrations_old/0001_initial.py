# Generated by Django 5.0.6 on 2024-10-30 06:13

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amaatra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CETRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('registration_number', models.CharField(max_length=20)),
                ('taken_kcet', models.BooleanField(default=False)),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('campus', models.CharField(blank=True, max_length=100, null=True)),
                ('kcet_rank', models.IntegerField(blank=True, null=True)),
                ('kcet_registration_number', models.CharField(blank=True, max_length=20, null=True)),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ECTransportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.BigIntegerField()),
                ('parent_phone_number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(max_length=10)),
                ('registration_no', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='ec_transportation/')),
                ('program', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
                ('pickup_point', models.CharField(max_length=255)),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('category', models.CharField(max_length=400)),
                ('priority', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-priority'],
            },
        ),
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.BigIntegerField()),
                ('designation', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('identity', models.CharField(max_length=100)),
                ('identity_number', models.CharField(max_length=30)),
                ('types_of_grievance', models.CharField(max_length=100)),
                ('your_grievance', models.TextField()),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='JEEMain1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('registration_number', models.CharField(max_length=20)),
                ('taken_jee_main1', models.BooleanField(default=False)),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('campus', models.CharField(blank=True, max_length=100, null=True)),
                ('jee_main1_rank', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('jee_main1_registration_number', models.CharField(blank=True, max_length=20, null=True)),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='JEEMain2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('registration_number', models.CharField(max_length=20)),
                ('taken_jee_main2', models.BooleanField(default=False)),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('campus', models.CharField(blank=True, max_length=100, null=True)),
                ('jee_main2_rank', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('jee_main2_registration_number', models.CharField(blank=True, max_length=20, null=True)),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PUCUpoloadMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('registration_number', models.CharField(max_length=20)),
                ('specialization', models.CharField(max_length=100)),
                ('campus', models.CharField(max_length=100)),
                ('intermediate_candidates', models.BooleanField(default=False)),
                ('physics', models.IntegerField()),
                ('chemistry', models.IntegerField()),
                ('mathematics_a', models.IntegerField()),
                ('mathematics_b', models.IntegerField(blank=True, null=True)),
                ('electronics', models.IntegerField(blank=True, null=True)),
                ('computer_science', models.IntegerField(blank=True, null=True)),
                ('aggregate_percentage', models.IntegerField()),
                ('upload_marks', models.ImageField(upload_to='puc_upload_marks/')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='RRTransportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.BigIntegerField()),
                ('parent_phone_number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(max_length=10)),
                ('registration_no', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='rr_transportation/')),
                ('program', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
                ('pickup_point', models.CharField(max_length=255)),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SSM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('class_admission', models.CharField(max_length=50)),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{10}$')])),
                ('details', models.TextField(blank=True, null=True)),
                ('username', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='user-profile/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=400)),
                ('campus', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ResetPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forget_password_token', models.CharField(max_length=255)),
                ('forget_password_token_created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
