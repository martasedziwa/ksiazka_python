"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import turtle


def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    """Rysuje spiralę Archimedesa, rozpoczynając od położenia początkowego.

    Argumenty:
      n: liczba odcinków liniowych do narysowania
      length: długość każdego odcinka
      a: stopień luźności spirali początkowej (większa wartość oznacza luźniejszą spiralę)
      b: stopień luźnego zwinięcia spirali (większa wartość oznacza luźniejszą spiralę)

    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta


# create the world and bob
bob = turtle.Turtle()
draw_spiral(bob, n=1000)

turtle.mainloop()

