"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import sys
import string
import random

# zmienne globalne
suffix_map = {}        # odwzorowanie przedrostków na listę przyrostków
prefix = ()            # bieżąca krotka słów


def process_file(filename, order=2):
    """Wczytuje pliku i przeprowadza analizę Markova.

    filename: łańcuch
    order: liczba całkowita słów w przedrostku

    Zwraca: odwzorowanie przedrostka na listę możliwych przyrostków.
    """
    fp = open(filename)
    skip_gutenberg_header(fp)

    for line in fp:
        for word in line.rstrip().split():
            process_word(word, order)


def skip_gutenberg_header(fp):
    """Wczytuje z fp do momentu znalezienia wiersza zakończonego nagłówkiem.

    fp: obiekt otwartego pliku
    """
    for line in fp:
        if line.startswith('*KONIEC*DROBNY DRUK!'):
            break


def process_word(word, order=2):
    """Przetwarza każde słowo.

    word: łańcuch
    order: liczba całkowita

    Podczas kilku pierwszych iteracji zapisywane są jedynie słowa.
    Później rozpoczynane jest dodawanie pozycji do słownika.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # w wypadku braku pozycji dla przedrostka jest on tworzony
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    """Generuje losowe słowa na podstawie przeanalizowanego tekstu.

    Rozpoczyna od losowego przedrostka ze słownika.

    n: liczba słów do wygenerowania
    """
    # wybieranie losowego przedrostka (bez ważenia częstością)
    start = random.choice(list(suffix_map.keys()))
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # jeśli początek nie występuje w odwzorowaniu, następuje przejście na koniec
            # oryginalnego tekstu, dlatego konieczne jest ponowne rozpoczęcie.
            random_text(n-i)
            return

        # wybieranie losowego przyrostka
        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)


def shift(t, word):
    """Tworzy nową krotkę przez usunięcie początku i dodanie słowa na końcu.
    
    t: krotka łańcuchów
    word: łańcuch

    Zwraca: krotka łańcuchów
    """
    return t[1:] + (word,)


def main(script, filename='emma.txt', n=100, order=2):
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Użycie: %d nazwa_pliku [liczba słów] [długość przedrostka]' % script)
    else: 
        process_file(filename, order)
        random_text(n)
        print()


if __name__ == '__main__':
    main(*sys.argv)
