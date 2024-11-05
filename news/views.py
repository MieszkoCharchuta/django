from datetime import datetime
from django.shortcuts import render
import requests


SOURCES = [
    {"id": "new-scientist", "name": "The New Scientist"},
    {"id": "techradar", "name": "ThechRadar"},
    {"id": "national-geographic", "name": "The National Geographic"},
    {"id": "mashable", "name": "Mashable"},
    {"id": "the-next-web", "name": "The Next Web"},
]


# Create your views here.
def index_view(request, source="new-scientist"):
    API_KEY = "ac243786048c44f49524eab15809b7cb"

    url = (
        "https://newsapi.org/v2/everything?"
        f"sources={source}&"
        f"pageSize=15&"
        f"apiKey={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()
    context = {
        "newsapi": data,
        "sources": SOURCES,
        "active_source": source,
    }
    return render(request, "news/index.html", context)


def lotto_view(request):
    url = "http://www.mbnet.com.pl/dl.txt"
    response = requests.get(url)

    last_draw_data = ""
    data = ""

    if response.status_code == 200:
        data = response.text.strip().splitlines()
        last_draw = data[-1]
        last_draw_data = last_draw.split()

    draw1_date = last_draw_data[1]
    draw1_numbers = [number.strip("") for number in last_draw_data[2].split(",")]

    total_draws = len(data)

    number_frequency = {i: 0 for i in range(1, 50)}

    for line in data:
        draw_data = line.split()
        draw_numbers = [int(number) for number in draw_data[2].split(",")]
        for number in draw_numbers:
            number_frequency[number] += 1

    total_numbers_drawn = total_draws * len(draw1_numbers)
    stats = []
    for number in range(1, 50):
        count = number_frequency[number]
        percentage = (count / total_numbers_drawn) * 100
        stats.append({"number": number, "count": count, "percentage": percentage})

    draw_date_str = draw1_date
    draw_date = datetime.strptime(draw_date_str, "%d.%m.%Y")
    draw_date = draw_date.replace(hour=22, minute=0, second=0)

    current_time = datetime.now()

    context = {
        "draw_date": draw_date,
        "draw_numbers": draw1_numbers,
        "total_draws": total_draws,
        "stats": stats,
        "now": current_time,
    }

    return render(request, "news/lotto.html", context)
