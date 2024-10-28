# Django: Baza danych (modele, queryset)

## Zadanie 1
Zmodyfikuj kod szablonu `blog/post_list.html`, aby wyświetlał komunikat *No posts to show*, gdy baza nie zawiera żadnych postów.

**Wskazówka**: Do rozwiązywania tego zadania możesz skorzystać z informacji zawartych na stronie dokumentacji Django (https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#for-empty).


## Zadanie 2
W modelach aplikacji blog, w tabeli `Post` dodaj nową kolumnę będącą datą publikacji postu (`date_publish`).

```python
date_publish = models.DateTimeField(blank=True, null=True)
```

Dowiedz się co oznaczają argumenty `blank=True` i `null=True` (https://docs.djangoproject.com/en/5.1/ref/models/fields/#null lub https://stackoverflow.com/a/8609425).

Następnie uaktualnij strukturę bazy danych poprzez wykonanie poleceń `makemigrations` i `migrate`.


## Zadanie 3
Otwórz panel administracyjny projektu Django i ustaw przykładowe daty publikacji dla każdego postu w bazie danych. Wyświetl datę publikacji w szablonie `blog/post_list.html`.


## Zadanie 4
Użyj odpowiedniego zapytania „queryset” w funkcji `post_list_view`, aby posty uszeregowane były według daty publikacji od najnowszych do najstarszych. Wskazówka: https://docs.djangoproject.com/en/5.1/ref/models/querysets/#order-by   


## Zadanie 5
Do modelu tabeli Post dodaj pole `is_public`, które może przyjmować wartości logiczne (`True`/`False`), domyślnie `True`. 

**Wskazówka**: W wyborze odpowiedniego pola `is_public` oraz zdefiniowania wartości domyślnej dla tego pola mogą przydać się informacje na stronie dokumentacji Django (https://docs.djangoproject.com/en/5.1/ref/models/fields/)

Następnie zmodyfikuj kod w pliku `blog/views.py`, aby na stronie `post_list.html` wyświetlały się tylko te posty, których wartość pola `is_public` to `True`. Dzięki temu będziesz miał(a) możliwość decydowania, kiedy dany post ma zostać upubliczniony.


## Zadanie 6
W pliku `blog/models.py` dodaj tabelę dotyczącą autora postów. W panelu administracyjnym przypisz posty do autora. W widoku szczegółowym postu `blog/post_detail.html`, wyświetl, kto jest jego autorem.


## Zadanie 7
Dodaj funkcjonalność, aby po kliknięciu na autora postu w pliku `blog/post_list.html` pokazywały się wszystkie posty tego autora.


## Zadanie 8
Dowolnie sformatuj i nadaj funkcjonalności stronom `blog/post_list.html` i `blog/post_detail.html`, aby Ci się podobały.


## Zadanie 9
Utwórz aplikację `biotools`, która poprzez funkcję `seqcontent_view` będzie wyświetlała pod adresem `biotools/seqcontent` pustą stronę `seqcontent.html`. Na następnych zajęciach będziemy na tej stronie tworzyć formularz umożliwiający użytkownikowi przesłanie danych.


## Zadanie 10 (dla chętnych).
Przy dużej liczbie postów na stronie `blog/post_list.html` „scrollowanie” może być męczące. Dodaj paginację do listy postów tak, aby lista wyświetlała się w częściach (np. 3 posty na stronę). Zapoznaj się z Paginacją w Django: https://docs.djangoproject.com/en/5.1/topics/pagination/ 