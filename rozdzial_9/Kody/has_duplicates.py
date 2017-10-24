"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def has_duplicates(t):
    """Sprawdza, czy dowolny element pojawia się w ciągu więcej niż raz.

    Prosta wersja używająca pętli for.

    t: ciąg
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    """Sprawdza, czy dowolny element pojawia się w ciągu więcej niż raz.

    Szybsza wersja wykorzystująca zbiór.

    t: ciąg
    """
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))

    t = [1, 2, 3]
    print(has_duplicates2(t))
    t.append(1)
    print(has_duplicates2(t))

