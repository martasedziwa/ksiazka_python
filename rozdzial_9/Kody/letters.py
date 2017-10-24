"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import turtle

from polygon import circle, arc

# FUNKCJE PODSTAWOWE POZIOMU 0 
# fd, bk, lt, rt, pu, pd

def fd(t, length):
    t.fd(length)

def bk(t, length):
    t.bk(length)

def lt(t, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pd(t):
    t.pd()

def pu(t):
    t.pu()


# FUNKCJE PODSTAWOWE POZIOMU 1 to proste kombinacje funkcji podstawowych poziomu 0.
# Funkcje te nie mają warunków wstępnych ani końcowych.

def fdlt(t, n, angle=90):
    """Do przodu i w lewo"""
    fd(t, n)
    lt(t, angle)

def fdbk(t, n):
    """Do przodu i do tyłu, zakończenie w pozycji początkowej"""
    fd(t, n)
    bk(t, n)

def skip(t, n):
    """Podniesienie pióra i przemieszczenie"""
    pu(t)
    fd(t, n)
    pd(t)

def stump(t, n, angle=90):
    """Utworzenie linii pionowej i pozostawienie obiektu żółwia u samej góry skierowanego w prawo"""
    lt(t)
    fd(t, n)
    rt(t, angle)

def hollow(t, n):
    """Przemieszczenie obiektu żółwia w pionie i pozostawienie go u samej góry skierowanego w prawo"""
    lt(t)
    skip(t, n)
    rt(t)


# FUNKCJE PODSTAWOWE POZIOMU 2 używają funkcji podstawowych poziomów 0 i 1
# do rysowania słupków (elementy pionowe) i belek (elementy poziome)
# Funkcje podstawowe poziomu 2 ZAWSZE zwracają obiekt żółwia do położenia
# początkowego w pierwotnym kierunku.

def post(t, n):
    """Utworzenie linii pionowej i powrót do położenia początkowego"""
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    """Utworzenie linii poziomej do danej wysokości i powrót."""
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)

def hangman(t, n, height):
    """Utworzenie linii pionowej i poziomej do danej wysokości, a następnie powrót.
    Implementacja tego jest efektywna i okazuje się przydatna, ale
    pod względem semantycznym nie jest to przejrzyste."""
    stump(t, n * height)
    fdbk(t, n)
    lt(t)
    bk(t, n*height)
    rt(t)

def diagonal(t, x, y):
    """Utworzenie linii przekątnej do danego przesunięcia x, y i powrót."""
    from math import atan2, sqrt, pi
    angle = atan2(y, x) * 180 / pi
    dist = sqrt(x**2 + y**2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, height):
    diagonal(t, -n/2, height*n)
    diagonal(t, n/2, height*n)

def bump(t, n, height):
    """Utworzenie wypukłości o promieniu n dla height*n 
    """
    stump(t, n*height)
    arc(t, n/2.0, 180)
    lt(t)
    fdlt(t, n*height+n)


"""
Wszystkie funkcje rysujące litery mają warunek wstępny taki, że
obiekt żółwia znajduje się w lewym dolnym narożniku litery,
a także warunek końcowy taki, że obiekt żółwia znajduje się w 
prawym dolnym narożniku, a ponadto skierowany jest kierunku
początkowym.

Wszystkie funkcje pobierają obiekt żółwia jako pierwszy argument
oraz wielkość (n) jako drugi. Większość liter ma szerokość (n) jednostek
i wysokość (2n) jednostek.

"""

def draw_a(t, n):
    diagonal(t, n/2, 2*n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n/2, 2*n)

def draw_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n/2)

def draw_c(t, n):
    hangman(t, n, 2)
    fd(t, n)

def draw_d(t, n):
    bump(t, 2*n, 0)
    skip(t, n)

def draw_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    draw_ef(t, n)
    fd(t, n)

def draw_f(t, n):
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    hangman(t, n, 2)
    fd(t, n/2)
    beam(t, n/2, 2)
    fd(t, n/2)
    post(t, n)

def draw_h(t, n):
    post(t, 2*n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2*n)

def draw_i(t, n):
    beam(t, n, 2)
    fd(t, n/2)
    post(t, 2*n)
    fd(t, n/2)

def draw_j(t, n):
    beam(t, n, 2)
    arc(t, n/2, 90)
    fd(t, 3*n/2)
    skip(t, -2*n)
    rt(t)
    skip(t, n/2)

def draw_k(t, n):
    post(t, 2*n)
    stump(t, n, 180)
    vshape(t, 2*n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    post(t, 2*n)
    fd(t, n)

def draw_n(t, n):
    post(t, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)
    post(t, 2*n)

def draw_m(t, n):
    post(t, 2*n)
    draw_v(t, n)
    post(t, 2*n)

def draw_o(t, n):
    skip(t, n)
    circle(t, n)
    skip(t, n)

def draw_p(t, n):
    bump(t, n, 1)
    skip(t, n/2)

def draw_q(t, n):
    draw_o(t, n)
    diagonal(t, -n/2, n)

def draw_r(t, n):
    draw_p(t, n)
    diagonal(t, -n/2, n)

def draw_s(t, n):
    fd(t, n/2)
    arc(t, n/2, 180)
    arc(t, n/2, -180)
    fdlt(t, n/2, -90)
    skip(t, 2*n)
    lt(t)

def draw_t(t, n):
    beam(t, n, 2)
    skip(t, n/2)
    post(t, 2*n)
    skip(t, n/2)

def draw_u(t, n):
    post(t, 2*n)
    fd(t, n)
    post(t, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    vshape(t, n, 2)
    skip(t, n/2)

def draw_w(t, n):
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    diagonal(t, n, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    diagonal(t, -n/2, 2*n)
    diagonal(t, n/2, 2*n)
    skip(t, n/2)

def draw_y(t, n):
    skip(t, n/2)
    stump(t, n)
    vshape(t, n, 1)
    rt(t)
    fdlt(t, n)
    skip(t, n/2)

def draw_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2*n)
    fd(t, n)

def draw_(t, n):
    # draw a space
    skip(t, n)

if __name__ == '__main__':

    # Tworzenie i pozycjonowanie obiektu żółwia
    size = 20
    bob = turtle.Turtle()

    for f in [draw_h, draw_e, draw_l, draw_l, draw_o]:
        f(bob, size)
        skip(bob, size)

    turtle.mainloop()
