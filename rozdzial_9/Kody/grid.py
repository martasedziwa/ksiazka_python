"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

# Oto prostsze rozwiązanie w wypadku wersji "dwa na dwa"
# siatki.

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
    

# Oto trudniejsze rozwiązanie w wypadku wersji "cztery na cztery"
# siatki.

def one_four_one(f, g, h):
    f()
    do_four(g)
    h()

def print_plus():
    print('+', end=' ')

def print_dash():
    print('-', end=' ')

def print_bar():
    print('|', end=' ')

def print_space():
    print(' ', end=' ')

def print_end():
    print()

def nothing():
    "nie wykonuj żadnego działania"

def print1beam():
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_bar, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, nothing)

print_grid()

comment = """
Po utworzeniu wersji roboczej siatki 4x4 zauważyłem, że wiele funkcji
miało identyczną strukturę: miały one wykonać jakieś działanie,
kolejne działanie cztery razy, a następnie jeszcze jedno działanie jednokrotnie.

Z tego powodu napisałem funkcję one_four_one pobierającą trzy funkcje
jako argumenty. Funkcja wywołuje jednokrotnie pierwszą funkcję, a następnie
używa funkcji do_four do czterokrotnego wywołania drugiej funkcji.
Na końcu funkcja wywołuje trzecią funkcję.

Zmodyfikowałem następnie funkcje print1beam, print1post, print4beams, print4posts,
print_row i print_grid za pomocą funkcji one_four_one.

Programowanie to proces eksplorowania. Tworzenie wersji roboczej programu
umożliwia często wgląd w problem, co może doprowadzić do modyfikacji kodu
w celu uwzględnienia struktury rozwiązania.

--- Allen
"""

print(comment)
