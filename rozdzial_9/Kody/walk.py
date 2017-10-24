"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import os


def walk(dirname):
    """Wyświetla nazwy wszystkich plików w katalogu i jego podkatalogach.

    Jest to wersja podana w książce.

    dirname: nazwa katalogu w postaci łańcucha
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dirname):
    """Wyświetla nazwy wszystkich plików w katalogu i jego podkatalogach.

    Jets to rozwiązanie ćwiczenia korzystające z os.walk.

    dirname: nazwa katalogu w postaci łańcucha
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))


if __name__ == '__main__':
    walk('.')
    walk2('.')
    
