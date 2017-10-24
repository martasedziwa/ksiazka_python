"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Time:
    """Reprezentuje porę dnia.
       
    atrybuty: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Inicjalizuje obiekt Time.

        hour: int
        minute: int
        second: int lub float
        """
        minutes = hour * 60 + minute
        self.seconds = minutes * 60 + second

    def __str__(self):
        """Zwraca reprezentację łańcuchową czasu."""
        minutes, second = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def print_time(self):
        """Wyświetla reprezentację łańcuchową czasu."""
        print(str(self))

    def time_to_int(self):
        """Oblicza liczbę sekund, jakie upłynęły od północy."""
        return self.seconds

    def is_after(self, other):
        """Zwraca wartość True, jeśli t1 występuje po t2. W przeciwnym razie zwracana jest wartość False."""
        return self.seconds > other.seconds

    def __add__(self, other):
        """Dodaje dwa obiekty Time lub obiekt Time i liczbę.

        other: obiekt Time lub liczba sekund
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Dodaje dwa obiekty Time lub obiekt Time i liczbę."""
        return self.__add__(other)

    def add_time(self, other):
        """Dodaje dwa obiekty Time."""
        assert self.is_valid() and other.is_valid()
        seconds = self.seconds + other.seconds
        return int_to_time(seconds)

    def increment(self, seconds):
        """Zwraca nowy obiekt Time stanowiący sumę danego czasu i wartości seconds."""
        seconds += self.seconds
        return int_to_time(seconds)

    def is_valid(self):
        """Sprawdza, czy obiekt Time spełnia wymagania niezmienników."""
        return self.seconds >= 0 and self.seconds < 24*60*60


def int_to_time(seconds):
    """Tworzy nowy obiekt Time.

    seconds: całkowita liczba sekund, jakie upłynęły od północy
    """
    return Time(0, 0, seconds)


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print('Czy end występuje po start?')
    print(end.is_after(start))

    print('Użycie __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Przykład polimorfizmu')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()
