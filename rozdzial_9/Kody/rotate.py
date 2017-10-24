"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def rotate_letter(letter, n):
    """Obraca literę o n pozycji. Nie powoduje to zmiany innych znaków.

    letter: łańcuch jednoliterowy
    n: liczba całkowita

    Zwraca: łańcuch jednoliterowy
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Obraca literę o n pozycji.

    word: łańcuch
    n: liczba całkowita

    Zwraca: łańcuch
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))
