# Django: szablony, pliki statyczne, organizacja urls

## Zadanie 1.
Strona [http://www.mbnet.com.pl/dl.txt](http://www.mbnet.com.pl/dl.txt) na bieżąco raportuje wyniki losowania Dużego Lotka od 1957 roku.

W aplikacji **news** utwórz szablon `lotto.html`, który będzie wyświetlał się pod adresem `/news/lotto/` poprzez funkcję `lotto_view()` pokazując datę i liczby ostatniego (najnowszego) losowania Dużego Lotka.


## Zadnie 2.
Rozszerz funkcję `lotto_view()` oraz szablon `lotto.html`, aby pokazać:
* Łączną liczbę wszystkich losowań Dużego Lotka, które odbyły się od 1957 roku do teraz.
* Utwórz również tabelę w szablonie pokazującą jak często wylosowana została każda liczba (1-49). Tabela powinna mieć trzy kolumny: liczba (1-49), zliczenie ile razy liczba została wylosowana, procentowy udział tej liczby z wszystkich wylosowanych liczb.


## Zadanie 3.
Użyj filtra `floatformat` w szablonie według [dokumentacji Django](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#floatformat), aby zaokrąglić procentowy udział liczb do dwóch miejsc po przecinku.


## Zadanie 4 (dla chętnych).
Przedstaw datę ostatniego losowania w szablonie, aby pokazany był czas jaki od niej upłynął. Na przykład: 4 days and 1 hour ago.

*Wskazówka*: Przydatny będzie wbudowany moduł Pythona `datatime` i funkcja `strptime`. Datę prześlij do szablonu HTML i skorzystaj z filtra `timesince` (https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#timesince).


## Zadanie 5 (dla chętnych).
Dostosuj wygląd całego projektu, aby Ci się podobał.