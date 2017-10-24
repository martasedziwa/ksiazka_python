"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import string
import turtle

"""
W celu użycia tego programu maszyny do pisania konieczne jest zapewnienie
modułu o nazwie letters.py, który zawiera funkcje o nazwach, takich jak like draw_a, draw_b itp.
"""

# Sprawdzenie, czy czytelnik zapewnił moduł letters.py
try:
    import letters
except ImportError as e:
    message = e.args[0]
    if message.startswith('Brak modułu'):
        raise ImportError(message + 
                          '\nMusisz zapewnić moduł o nazwie letters.py')


def teleport(t, x, y):
    """Przemieszcza obiekt Turtle bez rysowania linii.

    Warunek końcowy: pióro nie jest używane

    t: obiekt Turtle
    x: współrzędna
    y: współrzędna
    """
    t.pu()
    t.goto(x, y)
    t.pd()


def keypress(char):
    """Obsługuje zdarzenie po naciśnięciu klawisza przez użytkownika.

    Sprawdzenie, czy istnieje funkcja o właściwej nazwie. W przeciwnym razie
    wyświetlany jest komunikat o błędzie.

    char: łańcuch, litera do narysowania
    """
    # W wypadku rysowania w dalszym ciągu poprzedniej litery stosowany jest wariant awaryjny
    if bob.busy:
        return
    else:
        bob.busy = True

    # Określenie funkcji do wywołania i wykonanie tej operacji
    try:
        name = 'draw_' + char
        func = getattr(letters, name)
    except AttributeError:
        print("Nie wiem, jak narysować znak ", char)
        bob.busy = False
        return

    func(bob, size)

    letters.skip(bob, size/2)
    bob.busy = False


def carriage_return():
    """Przemieszczenie na początek następnego wiersza.
    """
    teleport(bob, -180, bob.ycor() - size*3)
    bob.busy = False


def presser(char):
    """Zwraca obiekt funkcji realizujący naciśnięcie klawisza.

    char: znak do narysowania w momencie wykonania funkcji

    returns: funkcja bez argumentów
    """
    def func():
        keypress(char)
    return func


# Tworzenie i pozycjonowanie obiektu Turtle
size = 20
bob = turtle.Turtle()
bob.busy = False
teleport(bob, -180, 150)

# Informowanie o wywołaniu funkcji keypress po naciśnięcie klawisza przez użytkownika
screen = bob.getscreen()

for char in string.ascii_lowercase:
    screen.onkey(presser(char), char)

screen.onkey(carriage_return, 'Return')

screen.listen()
turtle.mainloop()
