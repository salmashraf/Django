# Generated by Django 4.1.4 on 2023-01-07 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dress',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
