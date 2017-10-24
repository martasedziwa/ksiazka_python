"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def most_frequent(s):
    """Sortuje litery w s w odwrotnej kolejności częstości.

    s: łańcuch

    Zwraca: lista liter
    """
    hist = make_histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res
    

def make_histogram(s):
    """Utworzenie odwzorowania liter na liczbę ich wystąpień w s.

    s: łańcuch

    Zwraca: odwzorowanie litery na częstość
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def read_file(filename):
    """Zwraca zawartość pliku jako łańcuch."""
    return open(filename).read()


if __name__ == '__main__':
    string = read_file('emma.txt')
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)
