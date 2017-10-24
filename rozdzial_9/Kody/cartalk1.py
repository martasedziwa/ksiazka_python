"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def is_triple_double(word):
    """Sprawdza, czy słowo zawiera trzy kolejne dwukrotnie powtórzone litery.
    
    word: string

    Zwraca: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_double():
    """Wczytuje listę słów i wyświetla słowa z trzema kolejnymi dwukrotnie powtórzonymi literami."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Oto wszystkie słowa na liście, które zawierają')
print('trzy kolejne dwukrotnie powtórzone litery.')
find_triple_double()
print('')


