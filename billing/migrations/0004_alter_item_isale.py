# Generated by Django 4.0.4 on 2022-08-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='isale',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True),
        ),
    ]