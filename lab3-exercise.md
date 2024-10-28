# Django: aplikacja News, przesyłanie argumentów w url, models.py

## Zadanie 1.
Utwórz aplikację **weather**, która będzie pobierała informacje o aktualnej pogodzie. Informacje te znajdują się w serwisie https://wttr.in/. Na przykład pogoda dla Poznania w formacie JSON znajduje się pod adresem: https://wttr.in/Poznan?format=j1.

Aplikacja weather w projekcie Django powinna domyślnie (`http://localhost:8000/weather/`) wyświetlać informacje na temat pogody w Poznaniu (np. temperatura, ciśnienie, data obserwacji pogodowej). Dodaj również link do aplikacji weather w głównym Menu na stronie (`myapp/base.html`).


## Zadanie 2.
W aplikacji weather dodaj możliwość wyświetlania danych pogodowych dla kilku innych miast (np. London, Berlin). Na przykład, pod adresem http://localhost:8000/weather/London/ powinny zostać wyświetlone informacje o pogodzie dotyczące Londynu. Domyślnie, pod adresem http://localhost:8000/weather/ powinny nadal być dane dotyczące Poznania.


## Zadanie 3.
Podobnie jak w aplikacji **news**, na stronie aplikacji weather umieść linki na stronie HTML do kilku przykładów miast.


## Zadanie 4.
Dostosuj wygląd aplikacji weather, aby Ci się podobał.