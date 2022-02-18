import requests
from bs4 import BeautifulSoup
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from googletrans import Translator

from CovidStatistics.models import CovidData
translator = Translator()


class CovidDataGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidData
        fields = ('id',
                  'country',
                  'population',
                  'total_infections',
                  'deaths',
                  'recovered',
                  'they_are_sick_now'
                  )


class CovidDataPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidData
        fields = ('country',
                  )

    def validate(self, attrs):
        country = attrs.get('country', None).lower()
        country = translator.translate(f'{country}', src='ru', dest='en').text.lower()
        if country:
            CovidUrl = f'https://index.minfin.com.ua/reference/coronavirus/geography/{country}/'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'}
            full_page = requests.get(CovidUrl, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')
            Population = soup.findAll("strong", {"class": "black"})[0].text
            Population = int(Population.replace(u'\xa0', u''))
            Total_infections = soup.findAll("strong", {"class": "gold"})[0].text
            Total_infections = int(Total_infections.replace(u'\xa0', u''))
            Deaths = soup.findAll("strong", {"class": "red"})[0].text
            Deaths = int(Deaths.replace(u'\xa0', u''))
            Recovered = soup.findAll("strong", {"class": "green"})[0].text
            Recovered = int(Recovered.replace(u'\xa0', u''))
            They_are_sick_now = soup.findAll("strong", {"class": "blue"})[0].text
            They_are_sick_now = int(They_are_sick_now.replace(u'\xa0', u''))
            attrs['country'] = country.title()
            attrs['population'] = Population
            attrs['total_infections'] = Total_infections
            attrs['deaths'] = Deaths
            attrs['recovered'] = Recovered
            attrs['they_are_sick_now'] = They_are_sick_now
        else:
            raise ValidationError('not valid country')
        return attrs
