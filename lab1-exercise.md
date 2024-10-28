## Wprowadzenie do Django (views, urls, templates) 

## Zadanie 1.
W aplikacji **myapp** dodaj stronę `about.html`, aby wyświetlana była pod adresem `/about/` i `/about-me/` poprzez funkcję `about_view()`. Po dodaniu strony about uaktualnij linki w szablonach html, aby można było przechodzić między stronami.


## Zadanie 2.
Rozszerz kod `views.py` aplikacji **myapp**, aby na stronie `about.html` wyświetlały się dwie losowe wartości (od 1 do 10) w zmiennych: `lucky_number` i `unlucky_number`. W szablonie `about.html` sprawdź, czy wartości obu zmiennych są równe - jeżeli tak to powinien dodatkowo pojawić się komunikat: *Don’t worry, be happy!*.


## Zadanie 3.
Poniżej znajduje się lista Pythona zawierająca języki programowania poruszane na zajęciach.

```python
mytech = [
    {
      'name': 'HTML',
      'url': 'https://www.w3schools.com/html/',
      'level': 'beginner'
    },
    {
      'name': 'CSS',
      'url': 'https://www.w3schools.com/css/',
      'level': 'beginner'
    },
    {
      'name': 'Bootstrap',
      'url': 'https://getbootstrap.com',
      'level': 'beginner'
    },
    {
      'name': 'Python',
      'url': 'https://www.python.org',
      'level': 'intermediate'
    },
    {
      'name': 'Django',
      'url': 'https://www.djangoproject.com',
      'level': 'beginner'      
    },    
]
```

Umieść powyższą listę wewnątrz funkcji `about_view`, przekaż listę do szablonu `about.html` i wyświetl w formie formie listy `<ul>` zawierającej linki HTML. Na przykład:

* [HTML](https://www.w3schools.com/html/): beginner
* [CSS](https://www.w3schools.com/css/): beginner
* [Bootstrap](https://getbootstrap.com): beginner
* [Python](https://www.python.org): intermediate
* [Django](https://www.djangoproject.com): beginner


## Zadanie 4 (dla chętnych)
W pliku https://ftp.ncbi.nlm.nih.gov/genbank/README.genbank znajduje się informacja dotycząca daty i numeru wersji aktualnej bazy GenBank.

```
...
GenBank Flat File Release 262.0 
...

Target Release Date:       August 15, 2024
...
```


W aplikacji **myapp** dodaj stronę `genbank.html`, aby była: wyświetlana pod adresem `/genbank/` i obsługiwana przez funkcję `genbank_view()`. Funkcja `genbank_view()` powinna otworzyć plik README.genbank z serwera i odczytać numer wersji oraz datę aktualnej bazy GenBank. Następnie, obie odczytane wartości powinny zostać przekazane do szablonu `genbank.html` i wyświetlone na stronie. Wskazówka: Wbudowany moduł Pythona `urllib.request` umożliwia otwarcie i przeczytanie pliku z internetu.
