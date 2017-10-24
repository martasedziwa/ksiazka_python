"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def read_dictionary(filename='c06d'):
    """Wczytuje plik i buduje słownik odwzorowujący
    każde słowo na łańcuch opisujący jego podstawową wymowę.
    
    Dodatkowe wymowy są dodawane do słownika z liczbą (w nawiasach okrągłych)
    na końcu klucza, dlatego klucz drugiej wymowy w wypadku słowa
    abdominal to abdominal(2).

    filename: łańcuch
    Zwraca: odwzorowanie łańcucha na wymowę
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # pominięcie komentarzy
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d


if __name__ == '__main__':
    d = read_dictionary()
    for k, v in d.items():
        print(k, v)
