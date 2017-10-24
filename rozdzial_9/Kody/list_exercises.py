"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import random


def nested_sum(t):
    """Oblicza sumę wszystkich liczb na liście list.
   
    t: lista list liczb

    Zwraca: liczba
    """
    total = 0
    for nested in t:
        total += sum(nested)
    return total


def cumsum(t):
    """Oblicza skumulowaną sumę liczb w t.

    t: lista liczb

    Zwraca: lista liczb
    """
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res


def middle(t):
    """Zwraca wszystkie elementy t, z wyjątkiem pierwszego i ostatniego.

    t: lista

    Zwraca: nowa lista
    """
    return t[1:-1]


def chop(t):
    """Usuwa pierwszy i ostatni element t.

    t: lista

    Zwraca: None
    """
    del t[0]
    del t[-1]


def is_sorted(t):
    """Sprawdza, czy lista jest posortowana.

    t: lista

    Zwraca: boolean
    """
    return t == sorted(t)


def is_anagram(word1, word2):
    """Sprawdza, czy dwa słowa to anagramy

    word1: łańcuch lub lista
    word2: łańcuch lub lista

    Zwraca: boolean
    """
    return sorted(word1) == sorted(word2)


def has_duplicates(s):
    """Zwraca wartość True, jeśli dowolny element pojawia się w ciągu więcej niż raz.

    s: łańcuch lub lista

    Zwraca: bool
    """
    # utworzenie kopii t w celu uniknięcia modyfikowania parametru
    t = list(s)
    t.sort()

    # sprawdzenie pod kątem sąsiadujących elementów, które są równe
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False


def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == '__main__':
    main()
