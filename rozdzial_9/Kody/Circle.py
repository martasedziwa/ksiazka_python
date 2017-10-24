"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import copy

from Point1 import Point, Rectangle, print_point
from Point1_soln import distance_between_points


class Circle:
    """Reprezentuje koło.

    Atrybuty: center, radius
    """


def point_in_circle(point, circle):
    """Sprawdza, czy punkt położony jest wewnątrz koła (lub na jego granicy).

    point: obiekt Point
    circle: obiekt Circle
    """
    d = distance_between_points(point, circle.center)
    print(d)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    """Sprawdza, czy narożniki prostokąta są w obrębie koła lub na jego granicy.

    rect: obiekt Rectangle
    circle: obiekt Circle
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Sprawdza, czy dowolny narożnik prostokąta jest w obrębie koła lub na jego granicy.

    rect: obiekt Rectangle
    circle: obiekt Circle
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()

