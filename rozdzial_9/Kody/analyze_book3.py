"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import random

from bisect import bisect

from analyze_book1 import process_file


def random_word(hist):
    """Wybiera losowe słowo z histogramu.

    Prawdopodobieństwo każdego słowa jest proporcjonalne do jego częstości.

    hist: odwzorowanie słowa na częstość
    """
    # DO_ZROBIENIA: Może to zostać szybciej uzyskane przez jednokrotne obliczenie częstości
    # skumulowanych i ponowne wykorzystywanie ich.

    words = []
    freqs = []
    total_freq = 0

    # Tworzenie listy słów i listy częstości skumulowanych
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # Wybór wartości losowej i znalezienie jego położenia na liście skumulowanej
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    return words[index]


def main():
    hist = process_file('emma.txt', skip_header=True)

    print("\n\nNiektóre słowa losowe z książki")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()

