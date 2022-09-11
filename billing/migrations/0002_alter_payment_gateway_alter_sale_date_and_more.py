# Generated by Django 4.0.4 on 2022-08-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='gateway',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='vehicle_number',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
