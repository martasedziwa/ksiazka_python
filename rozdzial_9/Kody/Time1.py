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


def print_time(t):
    """Wyświetla reprezentację łańcuchową czasu.

    t: obiekt Time
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def int_to_time(seconds):
    """Tworzy nowy obiekt Time.

    seconds: całkowita liczba sekund, jakie upłynęły od północy.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time):
    """Oblicza liczbę sekund, jakie upłynęły od północy.

    time: obiekt Time.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def add_times(t1, t2):
    """Dodaje dwa obiekty Time.

    t1, t2: Time

    Zwraca: Time
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def valid_time(time):
    """Sprawdza, czy obiekt Time spełnia wymagania niezmienników.

    time: Time

    Zwraca: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def main():
    # jeśli film rozpoczyna się w południe...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print('Czas rozpoczęcia:', end=' ')
    print_time(noon_time)

    # a czas trwania filmu to 109 minut...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print('Czas trwania:', end=' ')
    print_time(run_time)

    # O jakiej godzinie film się kończy?
    end_time = add_times(noon_time, run_time)
    print('Czas zakończenia:', end=' ')
    print_time(end_time)


if __name__ == '__main__':
    main()
