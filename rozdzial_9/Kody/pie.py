"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math
import turtle


def draw_pie(t, n, r):
    """Rysuje koło, a następnie dokonuje przejścia w miejsce po prawej stronie.

    t: obiekt Turtle
    n: liczba segmentów
    r: długość promienistych elementów
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()

    
def polypie(t, n, r):
    """Rysuje koło podzielone na promieniste segmenty.

    t: obiekt Turtle
    n: liczba segmentów
    r: długość promienistych elementów
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)


def isosceles(t, r, angle):
    """Rysuje trójkąt równoramienny.

    Obiekt Turtle rozpoczyna i kończy w wierzchołku skierowany w stronę środka podstawy.

    t: obiekt Turtle
    r: długość równych ramion
    angle: kąt wierzchołka w stopniach
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)


bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()

# rysowanie wielu wieloboków z różną liczbą boków
size = 40
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)

bob.hideturtle()
turtle.mainloop()

