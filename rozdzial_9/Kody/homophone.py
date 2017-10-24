"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from pronounce import read_dictionary


def make_word_dict():
    """Odczytuje słowa w pliku words.txt i zwraca katalog
    zawierający słowa jako klucze."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def homophones(a, b, phonetic):
    """Sprawdza, czy dwa słowa mogą zostać wymówione w taki sam sposób.

    Jeśli dowolnego słowa nie ma w katalogu wymaiania, zwracana jest wartość False.

    a, b: łańcuchy
    phonetic: odwzorowanie słów na kody wymawiania
    """
    if a not in phonetic or b not in phonetic:
        return False

    return phonetic[a] == phonetic[b]


def check_word(word, word_dict, phonetic):
    """Sprawdza, czy słowo ma następującą właściwość:
    usunięcie pierwszej litery zapewnia tak samo wymawiane słowo,
    a usunięcie drugiej litery daje słowo o identycznej wymowie.

    word: string
    word_dict: słownik ze słowami jako kluczami
    phonetic: odwzorowanie słów na kody wymawiania
    """
    word1 = word[1:] 
    if word1 not in word_dict:
        return False
    if not homophones(word, word1, phonetic):
        return False

    word2 = word[0] + word[2:]
    if word2 not in word_dict:
        return False
    if not homophones(word, word2, phonetic):
        return False

    return True


if __name__ == '__main__':
    phonetic = read_dictionary()
    word_dict = make_word_dict()

    for word in word_dict:
        if check_word(word, word_dict, phonetic):
            print(word, word[1:], word[0] + word[2:])
