# Generated by Django 4.0.5 on 2022-09-15 10:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='effectuerdonarge',
            name='typePersonne',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='effectuerdonnature',
            name='typePersonne',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='donateuruser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 15, 10, 52, 14, 548361, tzinfo=utc), verbose_name='last_login'),
        ),
    ]
