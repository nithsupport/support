# Generated by Django 5.0.6 on 2024-11-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_app', '0006_comedk_upload_marks_jeemain1_upload_marks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeemain2',
            name='crl_rank',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
