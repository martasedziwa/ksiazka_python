"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import copy
import math

from Point1 import Point, Rectangle


def distance_between_points(p1, p2):
    """Oblicza odległość między dwoma obiektami Point.

    p1: Point
    p2: Point

    Zwraca: wartość zmiennoprzecinkowa
    """
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist


def move_rectangle(rect, dx, dy):
    """Przemieszczenie prostokąta przez zmodyfikowanie obiektu jego narożnika.

    rect: obiekt Rectangle.
    dx: zmiana współrzędnej x (może być ujemna).
    dy: zmiana współrzędnej y (może być ujemna).
    """
    rect.corner.x += dx
    rect.corner.y += dy


def move_rectangle_copy(rect, dx, dy):
    """Przemieszczenie prostokąta i zwrócenie nowego obiektu Rectangle.

    rect: obiekt Rectangle.
    dx: zmiana współrzędnej x (can be negative).
    dy: zmiana współrzędnej y (can be negative).

    Zwraca: nowy obiekt Rectangle
    """
    new = copy.deepcopy(rect)
    move_rectangle(new, dx, dy)
    return new


def main():
    blank = Point()
    blank.x = 0
    blank.y = 0

    grosse = Point()
    grosse.x = 3
    grosse.y = 4

    print('distance', end=' ')
    print(distance_between_points(grosse, blank))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)
    print('move')
    move_rectangle(box, 50, 100)
    print(box.corner.x)
    print(box.corner.y)

    new_box = move_rectangle_copy(box, 50, 100)
    print(new_box.corner.x)
    print(new_box.corner.y)


if __name__ == '__main__':
    main()

