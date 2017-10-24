"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import time


def make_word_list1():
    """Wczytuje wiersze z pliku i buduje listę za pomocą funkcji append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def make_word_list2():
    """Wczytuje wiersze z pliku i buduje listę za pomocą operatora + listy."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'sekund')

start_time = time.time()
t = make_word_list2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'sekund')

