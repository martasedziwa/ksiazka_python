"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math


def factorial(n):
    """Oblicza rekurencyjnie silnię z n."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    """Oblicza przybliżenie liczby pi.

    Algorytm autorstwa Srinivasa Ramanujana dostępny pod adresem 
    https://pl.wikipedia.org/wiki/Pi
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        term = factor * num / den
        print (term)
        total += term
        
        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / total

print(estimate_pi())
