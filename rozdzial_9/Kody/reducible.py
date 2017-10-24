"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def make_word_dict():
    """Wczytuje listę słów i zwraca słownik."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    # Konieczne jest dodanie do listy słów jednoliterowych
    # Za słowo uważany jest również pusty łańcuch.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d


"""memo to słownik odwzorowujący każde słowo umożliwiające rozkład,
na listę jego elementów podrzędnych umożliwiających rozkład. Na początku
używany jest pusty łańcuch."""


memo = {}
memo[''] = ['']


def is_reducible(word, word_dict):
    """Jeśli słowo umożliwia rozkład, zwracana jest lista jego elementów podrzędnych umożliwiających rozkład.

    Dodawana jest również pozycja do słownika memo.

    Łańcuch umożliwia rozkład, jeśli zawiera co najmniej jeden element podrzędny
    umożliwiający rozkład. Pusty łańcuch też umożliwia rozkład.

    word: łańcuch
    word_dict: słownik ze słowami w postaci kluczy
    """
     # jeśli dane słowo zostało już sprawdzone, zwracana jest odpowiedź
    if word in memo:
        return memo[word]

     # sprawdzenie każdego elementu podrzędnego i utworzenie listy słów umożliwiających rozkład
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)

    # zapamiętanie i zwracanie wyniku
    memo[word] = res
    return res


def children(word, word_dict):
    """Zwraca listę wszystkich słów, które mogą zostać uzyskane przez usunięcie jednej litery.

    word: łańcuch

    Zwraca: lista łańcuchów
    """
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res


def all_reducible(word_dict):
    """Sprawdza wszystkie słowa w word_dict i zwraca listę słów umożliwiających rozkład.
    
    word_dict: słownik ze słowami w postaci kluczy
    """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_trail(word):
    """Wyświetla ciąg słów redukujący dane słowo do postaci pustego łańcucha.

    W wypadku istnienia więcej niż jednej opcji wyboru wybierana jest pierwsza z nich. 

    word: łańcuch
    """
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word, word_dict)
    print_trail(t[0])


def print_longest_words(word_dict):
    """Znajduje najdłuższe słowa umożliwiające rozkład i wyświetla je.

    word_dict: słownik poprawnych słów
    """
    words = all_reducible(word_dict)

    # użycie DSU do sortowania według długości słów
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # wyświetlanie pięciu najdłuższych słów
    for _, word in t[0:5]:
        print_trail(word)
        print('\n')


if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_words(word_dict)
