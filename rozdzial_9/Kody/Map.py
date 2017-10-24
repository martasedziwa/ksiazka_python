"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class LinearMap:
    """Prosta implementacja odwzorowania używającego listy krotek, gdzie
    każda krotka to para klucz-wartość."""

    def __init__(self):
        self.items = []

    def add(self, k, v):
        """Dodaje nowy element odwzorowujący klucz (k) na wartość (v).
        Przyjęto, że klucze są unikatowe."""
        self.items.append((k, v))

    def get(self, k):
        """Wyszukuje klucz (k) i zwraca odpowiednią wartość
        lub zgłasza błąd KeyError, gdy nie znaleziono klucza."""
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError


class BetterMap:
    """Szybsza implementacja odwzorowania używającego listy obiektów LinearMap
    i funkcji wbudowanej hash() do określenia, jaki obiekt LinearMap
    ma zostać umieszczony w każdym kluczu."""

    def __init__(self, n=100):
        """Dołącza (n) obiektów LinearMap do (self)."""
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        """Znajduje właściwy obiekt LinearMap dla klucza (k)."""
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        """Dodaje nowy element do odpowiedniego obiektu LinearMap dla klucza (k)."""
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        """Znajduje właściwy obiekt LinearMap dla klucza (k) i wyszukuje w nim (k)."""
        m = self.find_map(k)
        return m.get(k)


class HashMap:
    """Implementacja tablicy mieszającej przy użyciu obiektu BetterMap,
    który tak się powiększa, że liczba elementów nigdy nie osiąga liczby
    obiektów LinearMaps.
    
    Zamortyzowany koszt dodawania powinien wynosić O(1), pod warunkiem, że
    implementacja sumy w operacji zmiany wielkości jest liniowa."""

    def __init__(self):
        """Rozpoczyna od 2 obiektów LinearMap i 0 elementów."""
        self.maps = BetterMap(2)
        self.num = 0

    def get(self, k):
        """Wyszukuje klucz (k) i zwraca odpowiednią wartość
        lub zgłasza błąd KeyError, gdy nie znaleziono klucza."""
        return self.maps.get(k)

    def add(self, k, v):
        """Zmienia w razie potrzeby wielkość odwzorowania i dodaje nowy element."""
        if self.num == len(self.maps.maps):
            self.resize()

        self.maps.add(k, v)
        self.num += 1

    def resize(self):
        """Tworzy nowe, dwukrotnie większe odwzorowanie i dokonuje ponownego mieszania elementów."""
        new_map = BetterMap(self.num * 2)

        for m in self.maps.maps:
            for k, v in m.items:
                new_map.add(k, v)

        self.maps = new_map


def main():
    import string

    m = HashMap()
    s = string.ascii_lowercase

    for k, v in enumerate(s):
        m.add(k, v)

    for k in range(len(s)):
        print(k, m.get(k))


if __name__ == '__main__':
    main()
