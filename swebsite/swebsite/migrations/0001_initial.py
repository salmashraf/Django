# Generated by Django 4.1.4 on 2022-12-31 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('length', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('description', models.TextField()),
            ],
        ),
    ]
