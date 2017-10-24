"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


from inlist import in_bisect, make_word_list


def reverse_pair(word_list, word):
    """Sprawdza, czy słowo zastrzeżone pojawia się w word_list.

    word_list: lista łańcuchów
    word: łańcuch
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])


