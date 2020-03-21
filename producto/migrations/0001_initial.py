# Generated by Django 3.0.4 on 2020-03-21 15:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=255, null=True)),
                ('descripcion', models.CharField(max_length=255, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=19)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2020, 3, 21, 15, 55, 9, 139229, tzinfo=utc))),
            ],
        ),
    ]
