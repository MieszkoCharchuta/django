# Django - aplikacja Biotools (formularze)

## Zadanie 1
Rozszerz kod w szablonie `biotools/seqcontent.html`, aby wyniki przedstawione były w formie tabeli HTML.


## Zadanie 2
Rozszerz kod w funkcji `seqcontent_view` oraz w szablonie `biotools/seqcontent.html`, aby w wynikach podana była również informacja o długości sekwencji.


## Zadanie 3
Rozszerz kod funkcji `count_words()` z pliku `biotools/utils.py`, aby wyniki obejmowały - oprócz zliczeń - procentowy udział każdego słowa w sekwencji. Umieść procentowy udział słów w trzeciej kolumnie tabeli pliku `biotools/seqcontent.html`.


## Zadanie 4
W aplikacji biotools utwórz nową stronę `biotools/revcomp.html`. W pliku `biotools/forms.py` utwórz nowy formularz, dzięki któremu użytkownik będzie mógł podać sekwencję DNA na stronie `biotools/revcomp.html`. Po przesłaniu formularza na stronie powinna się wyświetlić sekwencja odwrotnie komplementarna do wejściowej sekwencji użytkownika.

```python
ATGCATGGCTA     # input
TAGCCATGCAT     # reverse_complement
```

## Zadanie 5
W pliku `biotools/forms.py` dodaj odpowiednią metodę do utworzonego formularza, aby w polu sekwencji można było również podać sekwencję w formacie FASTA.


## Zadanie 6.
Dowolnie sformatuj szablony i funkcjonalności związane z aplikacją biotools, aby Ci się podobały.


## Zadanie 7* (dla chętnych)
W pliku `biotools/forms.py` dodaj pole do utworzonego formularza, aby użytkownik mógł wybrać jedną z trzech metod: `reverse complement`, `reverse`, oraz `complement`.

**Wskazówka**: StackOverflow: https://stackoverflow.com/questions/4788388/how-do-i-use-djangos-form-framework-for-select-options

Następnie zmodyfikuj kod w pliku `biotools/views.py`, aby wykonywał na sekwencji metodę wybraną w formularzu. Na przykład po wyborze w formularzu metody `reverse` sekwencja powinna zostać wyświetlona jedynie w odwrotnym kierunku.


## Zadanie 8* (dla chętnych)
W aplikacji `biotools` utwórz nową stronę `biotools/random_dna.html` i utwórz kod, który będzie generował losową sekwencję DNA o podanej przez użytkownika długości (min. 20 nukleotdyów, max. 10000 nukleotydów). W formularzu uwzględnij również możliwość podania prawdopodobieństwa wystąpienia każdego z nukleotdów (domyślnie nukleotdy występują z jednakowym prawdopodobieństwem, suma prawdopodobieństw musi być równa 1).