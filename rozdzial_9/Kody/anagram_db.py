"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import shelve
import sys

from anagram_sets import all_anagrams, signature


def store_anagrams(filename, anagram_map):
    """Przechowuje anagramy ze słownika w zmiennej shelf.

    filename: nazwa pliku łańcuchów tablicy shelf
    anagram_map: słownik odwzorowujący łańcuchy na listę anagramów
    """
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(filename, word):
    """Wyszukuje słowo w zmiennej shelf i zwraca listę jego anagramów.

    filename: nazwa pliku łańcuchów zmiennej shelf
    word: słowo do wyszukania
    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


def main(script, command='make_db'):
    if command == 'make_db':
        anagram_map = all_anagrams('words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))


if __name__ == '__main__':
    main(*sys.argv)
    
