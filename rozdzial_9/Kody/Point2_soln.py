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
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        """Dodaje obiekt Point lub krotkę."""
        if isinstance(other, Point):
            return self.add_point(other)
        elif isinstance(other, tuple):
            return self.add_tuple(other)
        else:
            msg = "Obiekt Point nie ma informacji o sposobie dodania typu " + type(other)
            raise TypeError(msg)

    def add_point(self, other):
        """Dodaje punkt."""
        return Point(self.x + other.x, self.y + other.y)

    def add_tuple(self, other):
        """Dodaje krotkę."""
        return Point(self.x + other[0], self.y + other[1])



def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1)
    print(p2)
    print(p1 + p2)
    print(p1 + (3, 4))

if __name__ == '__main__':
    main()

