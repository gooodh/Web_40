# Generated by Django 3.2.9 on 2022-01-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_userbookrelation_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=3, null=True),
        ),
    ]
