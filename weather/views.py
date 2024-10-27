from lib2to3.fixes.fix_input import context

import requests
from django.shortcuts import render
from .models import WeatherCondition
from datetime import datetime

SOURCES = [
	{'id': 'London', 'name': 'London'},
    {'id': 'Milan', 'name': 'Milan'},
    {'id': 'Berlin', 'name': 'Berlin'},
    {'id': 'Paris', 'name': 'Paris'},
    {'id': 'Madrid', 'name': 'Madrid'},
]

def index_view(request, source='Poznan'):
    url = f"https://wttr.in/{source}?format=j1"
    response = requests.get(url)
    data = response.json()

    # Extract the required fields
    current = data['current_condition'][0]
    weather_condition = WeatherCondition(
        area=data['nearest_area'][0]['areaName'][0]['value'],
        observed_at=datetime.strptime(current["localObsDateTime"], '%Y-%m-%d %I:%M %p'),
        temperature=current["temp_C"],
        pressure=current["pressure"]
    )
    # Standardized context setup (because I could not get it to work with bootstrapped base.html extensions
    context = {
        'weather': weather_condition,  # Makes `weather` variable available in the template
        'sources': SOURCES,
        'active_source': source,
    }
    return render(request, 'weather/index.html', context)

