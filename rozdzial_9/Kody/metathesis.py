"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import anagram_sets


def metathesis_pairs(d):
    """Wyświetla wszystkie pary słów różniących się w wyniku zamiany dwóch liter.

    d: odwzorowanie słowa na listę anagramów
    """
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


def word_distance(word1, word2):
    """Wyznacza liczbę różnic między dwoma słowami.

    word1, word2: łańcuchy

    Zwraca: liczba całkowita
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


if __name__ == '__main__':
    sets = anagram_sets.all_anagrams('words.txt')
    metathesis_pairs(sets)
