"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import bisect


def make_word_list():
    """Wczytuje wiersze z pliku i buduje listę za pomocą metody append.

    Zwraca: lista łańcuchów
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Sprawdza, czy słowo jest na liście za pomocą wyszukiwania z podziałem na połowę.

    Warunek wstępny: słowa na liście są sortowane

    word_list: lista łańcuchów
    word: string
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)


def in_bisect_cheat(word_list, word):
    """Sprawdza, czy słowo jest na liście za pomocą wyszukiwania z podziałem na połowę.

    Warunek wstępny: słowa na liście są sortowane

    word_list: lista łańcuchów
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'na liście', in_bisect(word_list, word))

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'na liście', in_bisect_cheat(word_list, word))


