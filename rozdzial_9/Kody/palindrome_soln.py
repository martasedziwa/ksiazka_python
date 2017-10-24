"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def first(word):
    """Zwraca pierwszy znak łańcucha."""
    return word[0]


def last(word):
    """Zwraca ostatni znak łańcucha."""
    return word[-1]


def middle(word):
    """Zwraca wszystkie znaki łańcucha, z wyjątkiem pierwszego i ostatniego."""
    return word[1:-1]


def is_palindrome(word):
    """Zwraca wartość True, jeśli słowo to palindrom."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('allen'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))

