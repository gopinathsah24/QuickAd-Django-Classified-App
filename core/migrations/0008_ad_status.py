# Generated by Django 3.0.5 on 2020-04-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_ad_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
