"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import sys

import matplotlib.pyplot as plt

from analyze_book1 import process_file


def rank_freq(hist):
    """Zwraca liste krotek (rank, freq).

    hist: odwzorowanie słowa na częstość

    Zwraca: lista krotek (rank, freq)
    """
    # sortowanie listy częstości w kolejności malejącej
    freqs = list(hist.values())
    freqs.sort(reverse=True)

    # wyliczenie rang i częstości 
    rf = [(r+1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(hist):
    """Wyświetla porównanie danych dotyczących rang i częstości.

    hist: odwzorowanie słowa na częstość
    """
    for r, f in rank_freq(hist):
        print(r, f)


def plot_ranks(hist, scale='log'):
    """Rysuje częstość w zestawieniu z rangą.

    hist: odwzorowanie słowa na częstość
    scale: łańcuch 'linear' lub 'log'
    """
    t = rank_freq(hist)
    rs, fs = zip(*t)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Wykres Zipf')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()


def main(script, filename='emma.txt', flag='plot'):
    hist = process_file(filename, skip_header=True)

    # either print the results or plot them
    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print('Użycie: zipf.py nazwa_pliku [print|plot]')


if __name__ == '__main__':
    main(*sys.argv)
