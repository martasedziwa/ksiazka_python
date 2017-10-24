"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


from datetime import datetime

# W celu uniknięcia duplikowania kodu importuję wszystko z Time1
from Time1 import *


def is_after(t1, t2):
    """Zwraca wartość True, jeśli t1 występuje po t2. W przeciwnym razie zwracana jest wartość False."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


def increment(t1, seconds):
    """Dodaje sekundy do obiektu Time."""
    assert valid_time(t1)
    seconds += time_to_int(t1)
    return int_to_time(seconds)


def mul_time(t1, factor):
    """Mnoży obiekt Time przez współczynnik factor."""
    assert valid_time(t1)
    seconds = time_to_int(t1) * factor
    return int_to_time(seconds)


def days_until_birthday(birthday):
    """Ile pozostało czasu do moich następnych urodzin?"""
    today = datetime.today()
    # Jeśli moje urodziny są w tym roku.
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    # Jeśli w tym roku już były, kiedy będą w następnym roku?
    if today > next_birthday:
        next_birthday = datetime(today.year+1, birthday.month, birthday.day)

    # Odejmowanie w wypadku obiektów datetime powoduje zwrócenie obiektu delty czasu
    delta = next_birthday - today
    return delta.days


def double_day(b1, b2):
    """Określa dzień, w którym jedna osoba jest dwukrotnie starsza od drugiej.

    b1: data i godzina urodzin młodszej osoby
    b2: data i godzina urodzin starszej osoby
    """
    assert b1 > b2
    delta = b1 - b2
    dday = b1 + delta
    return dday


def datetime_exercises():
    """Rozwiązania ćwiczeń."""

    # Wyświetla dzień tygodnia dla dzisiejszego dnia
    today = datetime.today()
    print(today.weekday())
    print(today.strftime('%A'))

    # Oblicza liczbę dni do następnych urodzin
    # (zauważ, że zwykle jest to zaokrąglane w dół)
    birthday = datetime(1967, 5, 2)
    print('Liczba dni do urodzin', end=' ')
    print(days_until_birthday(birthday))

    # Określa dzień, w którym jedna osoba jest dwukrotnie starsza od drugiej
    b1 = datetime(2006, 12, 26)
    b2 = datetime(2003, 10, 11)
    print('Podwójna data', end=' ')
    print(double_day(b1, b2))


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

    print('Czy to się kończy po rozpoczęciu?', end=' ')
    print(is_after(end_time, noon_time))

    print('Czas powrotu do domu', end=' ')
    travel_time = 600      # 10 minut
    home_time = increment(end_time, travel_time)
    print_time(home_time)

    race_time = Time()
    race_time.hour = 1
    race_time.minute = 34
    race_time.second = 5

    print('Czas półmaratonu', end=' ')
    print_time(race_time)

    distance = 13.1       # mile
    pace = mul_time(race_time, 1/distance)

    print('Czas przypadający na milę', end=' ')
    print_time(pace)

    datetime_exercises()


if __name__ == '__main__':
    main()
