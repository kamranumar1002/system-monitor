# Generated by Django 5.1.1 on 2025-02-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tblbenchmark',
            options={'verbose_name': 'Benchmark', 'verbose_name_plural': 'Benchmarks'},
        ),
        migrations.AlterModelOptions(
            name='tblclients',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='tblevent',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='tblsites',
            options={'verbose_name': 'Site', 'verbose_name_plural': 'Sites'},
        ),
        migrations.AlterModelOptions(
            name='tblsystem',
            options={'verbose_name': 'System', 'verbose_name_plural': 'Systems'},
        ),
        migrations.AlterField(
            model_name='tblevent',
            name='event_emaildelivery',
            field=models.IntegerField(default=0),
        ),
    ]
