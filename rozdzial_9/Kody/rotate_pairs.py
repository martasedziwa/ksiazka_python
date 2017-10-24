"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from rotate import rotate_word


def make_word_dict():
    """Wczytuje słowa w pliku words.txt i zwraca słownik
    zawierający słowa jako klucze."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    return d


def rotate_pairs(word, word_dict):
    """Wyświetla wszystkie słowa, które mogą być generowane przez obrót słowa.

    word: łańcuch
    word_dict: słownik ze słowami jako kluczami
    """
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)


if __name__ == '__main__':
    word_dict = make_word_dict()

    for word in word_dict:
        rotate_pairs(word, word_dict)
