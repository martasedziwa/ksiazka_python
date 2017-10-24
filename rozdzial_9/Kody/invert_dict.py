"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def invert_dict(d):
    """Odwraca słownik, zwracając odwzorowanie wartości na listę kluczy.

    Jeśli odwzorowanie kluczy na wartość pojawi się w d, w nowym słowniku
    wartość odwzorowywana jest na listę zawierającą klucz.
    
    d: dict

    Zwraca: dict
    """
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(d)
    for val in inverse:
        keys = inverse[val]
        print(val, keys)

