# Generated by Django 5.0.6 on 2024-11-20 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_app', '0003_alter_ssmfaq_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PESHospitalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='PESIMSRCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='PESPublicSchoolCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='PESUIMSRCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=400)),
            ],
        ),
        migrations.RemoveField(
            model_name='amaatrafaq',
            name='category',
        ),
        migrations.RemoveField(
            model_name='ssmfaq',
            name='category',
        ),
        migrations.CreateModel(
            name='PESHospitalFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('priority', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='support_app.peshospitalcategory')),
            ],
            options={
                'ordering': ['-priority'],
            },
        ),
        migrations.CreateModel(
            name='PESIMSRFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('priority', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='support_app.pesimsrcategory')),
            ],
            options={
                'ordering': ['-priority'],
            },
        ),
        migrations.CreateModel(
            name='PESPublicSchoolFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('priority', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='support_app.pespublicschoolcategory')),
            ],
            options={
                'ordering': ['-priority'],
            },
        ),
        migrations.CreateModel(
            name='PESUIMSRFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('priority', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='support_app.pesuimsrcategory')),
            ],
            options={
                'ordering': ['-priority'],
            },
        ),
        migrations.AddField(
            model_name='amaatrafaq',
            name='category',
            field=models.ManyToManyField(blank=True, to='support_app.amaatracategory'),
        ),
        migrations.AddField(
            model_name='ssmfaq',
            name='category',
            field=models.ManyToManyField(blank=True, to='support_app.ssmcategory'),
        ),
    ]
