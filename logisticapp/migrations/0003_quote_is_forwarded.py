# Generated by Django 4.2.7 on 2023-11-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticapp', '0002_quote_forwarded_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='is_forwarded',
            field=models.BooleanField(default=False),
        ),
    ]