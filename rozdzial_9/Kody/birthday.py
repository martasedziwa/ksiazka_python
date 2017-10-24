"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import random


def has_duplicates(t):
    """Zwraca wartość True, jeśli w ciągu dowolny element występuje więcej niż raz.

    t: list

    Zwraca: bool
    """
    # utworzenie kopii t w celu uniknięcia modyfikowania parametru
    s = t[:]
    s.sort()

    # sprawdzenie pod kątem sąsiednich elementów, które są równe
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def random_bdays(n):
    """Zwraca listę liczb całkowitych z zakresu od 1 do 365 dla długości n.

    n: int

    Zwraca: lista elementów typu int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    """Generuje przykładowe daty urodzin i określa liczbę duplikatów.

    num_students: liczba studentów w grupie
    num_samples: liczba grop do symulowania

    Zwraca: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count


def main():
    """Uruchamia symulację dat urodzin i wyświetla liczbę zgodności."""
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('W wypadku %d symulacji' % num_simulations)
    print('z %d studentami' % num_students)
    print(' %d symulacji miało co najmniej jedną zgodność.' % count)


if __name__ == '__main__':
    main()
