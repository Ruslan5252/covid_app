from django.db import models

class CovidData(models.Model):
    country = models.CharField('Страна',max_length=150)
    population = models.PositiveIntegerField('Население',default=0)
    total_infections = models.PositiveIntegerField('Всего зараженных',default=0)
    deaths = models.PositiveIntegerField('Смертельные исходы',default=0)
    recovered = models.PositiveIntegerField('Выздоровевшие',default=0)
    they_are_sick_now = models.PositiveIntegerField('Болеют прямо сейчас ',default=0)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Данные по Ковиду'
        verbose_name_plural = 'Данные по Ковиду'