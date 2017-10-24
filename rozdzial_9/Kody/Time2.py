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
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Zwraca reprezentację łańcuchową czasu."""
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        """Wyświetla reprezentację łańcuchową czasu."""
        print(str(self))

    def time_to_int(self):
        """Oblicza liczbę sekund, jakie upłynęły od północy."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        """Zwraca wartość True, jeśli t1 występuje po t2. W przeciwnym razie zwracana jest wartość False."""
        return self.time_to_int() > other.time_to_int()

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
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """Zwraca nowy obiekt Time stanowiący sumę danego czasu i wartości seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self):
        """Sprawdza, czy obiekt Time spełnia wymagania niezmienników."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True


def int_to_time(seconds):
    """Tworzy nowy obiekt Time.

    seconds: całkowita liczba sekund, jakie upłynęły od północy.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
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
