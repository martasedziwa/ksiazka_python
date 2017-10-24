"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from inlist import make_word_list, in_bisect


def interlock(word_list, word):
    """Sprawdza, czy słowo zawiera dwa „zazębiające się” słowa.

    word_list: lista łańcuchów
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
        

def interlock_general(word_list, word, n=3):
    """Sprawdza, czy słowo zawiera n „zazębiających się” słów.

    word_list: lista łańcuchów
    word: string
    n: liczba „zazębiających się” słów
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])


