"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def do_twice(func, arg):
    """Uruchamia dwukrotnie funkcję.

    func: obiekt funkcji
    arg: argument przekazywany funkcji
    """
    func(arg)
    func(arg)


def print_twice(arg):
    """Wyświetla dwukrotnie argument.

    arg: cokolwiek możliwe do wyświetlenia
    """
    print(arg)
    print(arg)


def do_four(func, arg):
    """Uruchamia funkcję cztery razy.

    func: obiekt funkcji
    arg: argument przekazywany funkcji
    """
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print_twice, 'spam')
print('')

do_four(print_twice, 'spam')
