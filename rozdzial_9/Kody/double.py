"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from datetime import datetime


def main():
    print("Dzisiejsza data i dzień tygodnia:")
    today = datetime.today()
    print(today)
    print(today.strftime("%A"))

    print("Data następnych urodzin i liczba dni, jaka do nich pozostała:")
    #s = input('Wprowadź datę urodzenia w formacie mm/dd/rrrr: ')
    s = '5/11/1967'
    bday = datetime.strptime(s, '%m/%d/%Y')

    next_bday = bday.replace(year=today.year)
    if next_bday < today:
        next_bday = next_bday.replace(year=today.year+1)
    print(next_bday)

    until_next_bday = next_bday - today
    print(until_next_bday)

    print("Aktualny wiek:")
    last_bday = next_bday.replace(year=next_bday.year-1)
    age = last_bday.year - bday.year
    print(age)

    print("Dotyczy osób urodzonych w następującym przedziale dat:")
    bday1 = datetime(day=11, month=5, year=1967)
    bday2 = datetime(day=11, month=10, year=2003)
    print(bday1)
    print(bday2)

    print("Podwójna data to")
    d1 = min(bday1, bday2)
    d2 = max(bday1, bday2)
    dd = d2 + (d2 - d1)
    print(dd)


if __name__ == '__main__':
    main()
