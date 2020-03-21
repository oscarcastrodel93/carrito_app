# Generated by Django 3.0.4 on 2020-03-21 19:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_auto_20200321_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='total_items',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 19, 51, 7, 716766, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 19, 51, 7, 715767, tzinfo=utc)),
        ),
    ]