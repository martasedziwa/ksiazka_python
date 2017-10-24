"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from analyze_book1 import process_file


def subtract(d1, d2):
    """Zwraca zbiór wszystkich kluczy występującymi w d1, lecz nie w d2.

    d1, d2: słowniki
    """
    return set(d1) - set(d2)


def main():
    hist = process_file('emma.txt', skip_header=True)
    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("Słowa w książce nieobecne na liście słów to:")
    for word in diff:
        print(word, end=' ')


if __name__ == '__main__':
    main()

