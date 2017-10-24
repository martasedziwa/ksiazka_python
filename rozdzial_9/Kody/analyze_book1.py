"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import random
import string

def process_file(filename, skip_header):
    """Tworzy histogram zawierający słowa z pliku.

    filename: string
    skip_header: typ boolean, okreśka, czy ma zostać pominięty nagłówek Gutenberga
   
    Zwraca: odwzorowanie każdego słowa na liczbę jego wystąpień.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, hist)

    return hist


def skip_gutenberg_header(fp):
    """Wczytuje z fp do momentu znalezienia wiersza zakończonego nagłówkiem.

    fp: otwieranie obiektu pliku
    """
    for line in fp:
        if line.startswith('*ZAKOŃCZ*DROBNYM DRUKIEM!'):
            break


def process_line(line, hist):
    """Dodaje słowa w wierszu do histogramu.

    Modyfikuje hist.

    line: string
    hist: histogram (odwzorowanie słowa na częstość)
    """
    # DO_ZROBIENIA: przebudowa za pomocą Counter

    # zastępowanie myślników spacjami przed podziałem
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in line.split():
        # usuwanie znaków interpunkcji i zamiana na małe litery
        word = word.strip(strippables)
        word = word.lower()

        # aktualizowanie histogramu
        hist[word] = hist.get(word, 0) + 1


def most_common(hist):
    """Tworzy listę par słowo-częstość zgodnie ze zmniejszającą się częstością.

    hist: odwzorowanie słowa na częstość

    Zwraca: lista par (częstość, słowo)
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t


def print_most_common(hist, num=10):
    """Wyświetla najczęstsze słowa histogramu wraz z ich częstościami.
    
    hist: histogram (odwzorowanie słowa na częstość)
    num: liczba słów do wyświetlenia
    """
    t = most_common(hist)
    print('Najczęstsze słowa to:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """Zwraca słownik z wszystkimi kluczami występującymi w d1, lecz nie w d2.

    d1, d2: słowniki
    """
    # DO_ZROBIENIA: ponowna implementacja za pomocą Counter
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


def total_words(hist):
    """Zwraca łaczną liczbę częstości histogramu."""
    return sum(hist.values())


def different_words(hist):
    """Zwraca liczbę różnych słów histogramu."""
    return len(hist)


def random_word(hist):
    """Wybiera losowe słowo z histogramu.

    Prawdopodobieństwo każdego słowa jest proporcjonalne do jego częstości.
    """
    # DO_ZROBIENIA: przebudowa za pomocą Counter
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)


def main():
    hist = process_file('emma.txt', skip_header=True)
    print('Łączna liczba słów:', total_words(hist))
    print('Liczba różnych słów:', different_words(hist))

    t = most_common(hist)
    print('Najczęstsze słowa to:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("Słowa w książce nieobecne na liście słów to:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nNiektóre słowa losowe z książki")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()


