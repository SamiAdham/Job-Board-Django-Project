# Generated by Django 3.0.7 on 2020-06-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='job/'),
            preserve_default=False,
        ),
    ]