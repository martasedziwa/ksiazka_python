"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def str_fill(i, n):
    """Zwraca i jako łańcuch z co najmniej n cyframi.

    i: int
    n: długość liczby całkowitej

    Zwraca: string
    """
    return str(i).zfill(n)


def are_reversed(i, j):
    """Sprawdza, czy i i j są odwrotnością siebie.

    i: int
    j: int

    Zwraca:bool
    """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):
    """Określa liczbę wystąpień palindromu dla daty urodzin.

    Zwraca liczbę razy, jaką w ciągu życia matki i córki
    dla ich dat urodzin występuje palindrom dla danej różnicy wieku.
    
    diff: różnica w wieku jako liczba całkowita
    flag: bool, jeśli True; wyświetla szczegóły
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff

        # Zakładając, że matka i córka nie mają urodzin w tym samym dniu,
        # w ciągu roku są dwie szanse na to, że daty ich urodzin utworzą 
        # palindrom.
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """Znajduje różnicę wieku jako rozwiązanie problemu.

    Wylicza możliwe różnice wieku między matką i córką, a
    ponadto dla każdej różnicy określa liczbę, jaką w ciągu ich
    życia występuje wiek będący odwrotnością drugiego wieku.
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1

print('diff  #instances')
check_diffs()

print()
print('córka  matka')
num_instances(18, True)
