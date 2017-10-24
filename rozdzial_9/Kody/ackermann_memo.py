"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

cache = {}

def ackermann(m, n):
    """Oblicza funkcję Ackermanna A(m, n)

    http://en.wikipedia.org/wiki/Ackermann_function

    n, m: nieujemne liczby całkowite
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]


print(ackermann(3, 4))
print(ackermann(3, 6))
