# Generated by Django 3.0.2 on 2020-01-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectorApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='state',
            field=models.CharField(choices=[(1, 'ACTIVE'), (2, 'ARCHIVE')], max_length=1),
        ),
    ]
