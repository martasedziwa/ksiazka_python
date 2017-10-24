"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import random


def sort_by_length(words):
    """Sortuje listę słów w odwrotnej kolejności według długości.

    Jest to wersja zawarta w książce stabilna w tym sensie, że słowa
    o tej samej długości pojawiają się w tej samej kolejności.

    words: lista łańcuchów

    Zwraca: lista łańcuchów
    """
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res


def sort_by_length_random(words):
    """Sortuje listę słów w odwrotnej kolejności według długości.

    Jest to rozwiązanie ćwiczenia niestabilne w tym sensie, że
    jeśli dwa słowa mają identyczną długość, ich kolejność na
    liście wyjściowej jest losowa.

    Działanie polega na rozszerzaniu listy krotek za pomocą kolumny
    liczb losowych. Gdy w pierwszej kolumnie występuje wynik,
    o kolejności listy wyjściowej decyduje kolumna liczb losowych.

    words: lista łańcuchów

    Zwraca: lista łańcuchów
    """
    t = []
    for word in words:
        t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res


if __name__ == '__main__':
    words = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

    t = sort_by_length_random(words)
    for x in t:
        print(x)
