"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def signature(s):
    """Zwraca sygnaturę danego łańcucha.

    Sygnatura to łańcuch zawierający wszystkie uporządkowane litery.

    s: string
    """
    # DO_ZROBIENIA: przebudowa za pomocą sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Znajduje wszystkie anagramy na liście słów.

    filename: nazwa pliku łańcuchów listy słów

    Zwraca: odwzorowanie każdego słowa na listę jego anagramów.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # DO_ZROBIENIA: przebudowa za pomocą defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Wyświetla zbiory anagramów w d.

    d: odwzorowanie słów na listę ich anagramów
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    """Wyświetla zbiory anagramów w d zgodnie ze zmniejszającą się wielkością.

    d: odwzorowanie słów na listę ich anagramów
    """
    # utworzenie listy (długość, pary słów)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sortowanie zgodnie z rosnącą długością
    t.sort()

    # wyświetlenie posortowanej listy
    for x in t:
        print(x)


def filter_length(d, n):
    """Wybiera tylko te słowa w d, które zawierają n liter.

    d: odwzorowanie słowa na listę anagramów
    n: całkowita liczba liter

    Zwraca: nowe odwzorowanie słowa na listę anagramów
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    anagram_map = all_anagrams('words.txt')
    print_anagram_sets_in_order(anagram_map)

    eight_letters = filter_length(anagram_map, 8)
    print_anagram_sets_in_order(eight_letters)
    
