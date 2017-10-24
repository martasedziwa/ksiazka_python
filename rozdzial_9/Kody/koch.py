"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import turtle


def koch(t, n):
    """Rysuje krzywą Kocha o długości n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Rysuje płatek (trójkąt z krzywą Kocha dla każdego boku)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()

