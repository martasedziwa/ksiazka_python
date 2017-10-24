"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Point:
    """Reprezentuje punkt w przestrzeni dwuwymiarowej.

    atrybuty: x, y
    """


def print_point(p):
    """Wyświetla obiekt Point w formacie zrozumiałym dla użytkownika."""
    print('(%g, %g)' % (p.x, p.y))


class Rectangle:
    """Reprezentuje prostokąt. 

    atrybuty: width, height, corner.
    """


def find_center(rect):
    """Zwraca punkt w środku prostokąta.

    rect: Rectangle

    Zwraca: nowy obiekt Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modyfikuje prostokąt przez zwiększenie jego szerokości i wysokości.

    rect: obiekt Rectangle.
    dwidth: zmiana szerokości (może być ujemna).
    dheight: zmiana wysokości (może być ujemna).
    """
    rect.width += dwidth
    rect.height += dheight


def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print('blank', end=' ')
    print_point(blank)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)


if __name__ == '__main__':
    main()

