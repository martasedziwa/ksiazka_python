"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def has_palindrome(i, start, length):
    """Sprawdza, czy reprezentacja łańcuchowa dla i ma palindrom.

    i: integer
    start: miejsce początkowe operacji w łańcuchu
    length: długość palindromu, dla którego ma miejsce sprawdzenie
    """
    s = str(i)[start:start+length]
    return s[::-1] == s

    
def check(i):
    """Sprawdza, czy liczba całkowita (i) ma żądane właściwości.

    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))


def check_all():
    """Wylicza liczby 6-cyfrowe i wyświetla wszystkich wygranych.
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


print('Oto możliwe odczyty drogomierza:')
check_all()
print()


