# Generated by Django 4.0.2 on 2022-02-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CovidStatistics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coviddata',
            name='Deaths',
        ),
        migrations.RemoveField(
            model_name='coviddata',
            name='Recovered',
        ),
        migrations.RemoveField(
            model_name='coviddata',
            name='They_are_sick_now',
        ),
        migrations.RemoveField(
            model_name='coviddata',
            name='Total_infections',
        ),
        migrations.AddField(
            model_name='coviddata',
            name='deaths',
            field=models.PositiveIntegerField(default=0, verbose_name='Смертельные исходы'),
        ),
        migrations.AddField(
            model_name='coviddata',
            name='recovered',
            field=models.PositiveIntegerField(default=0, verbose_name='Выздоровевшие'),
        ),
        migrations.AddField(
            model_name='coviddata',
            name='they_are_sick_now',
            field=models.PositiveIntegerField(default=0, verbose_name='Болеют прямо сейчас '),
        ),
        migrations.AddField(
            model_name='coviddata',
            name='total_infections',
            field=models.PositiveIntegerField(default=0, verbose_name='Всего зараженных'),
        ),
    ]
