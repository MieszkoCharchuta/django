from datetime import datetime
import requests

from django.shortcuts import render


CITIES = ["Poznan", "London", "Berlin", "New York"]


def index_view(request, city="Poznan"):
    URL = f"https://wttr.in/{city}?format=j1"
    response = requests.get(URL)
    data = response.json()
    context = {
        "cities": CITIES,
        "data": data,
        "active_city": city,
    }
    date_str = data["current_condition"][0]["localObsDateTime"]
    context["date"] = datetime.strptime(date_str, "%Y-%m-%d %H:%M %p")
    return render(request, "weather/index.html", context)
