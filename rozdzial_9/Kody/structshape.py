"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

"""
Moduł ten zapewnia funkcję structshape() pobierającą
obiekt dowolnego typu i zwracającą łańcuch podsumowujący
"kształt" struktury danych, czyli typ, wielkość i kompozycję.
"""

def structshape(ds):
    """Zwraca łańcuch opisujący "kształt" struktury danych.

    ds: dowolny obiekt języka Python

    Zwraca: łańcuch
    """
    typename = type(ds).__name__

    # obsługa ciągów
    sequence = (list, tuple, set, type(iter('')))
    if isinstance(ds, sequence):
        t = []
        for i, x in enumerate(ds):
            t.append(structshape(x))
        rep = '%s of %s' % (typename, listrep(t))
        return rep

    # obsługa słowników
    elif isinstance(ds, dict):
        keys = set()
        vals = set()
        for k, v in ds.items():
            keys.add(structshape(k))
            vals.add(structshape(v))
        rep = '%s of %d %s->%s' % (typename, len(ds), 
                                   setrep(keys), setrep(vals))
        return rep

    # obsługa innych typów
    else:
        if hasattr(ds, '__class__'):
            return ds.__class__.__name__
        else:
            return typename


def listrep(t):
    """Zwraca reprezentację łańcuchową listy łańcuchów typu.

    t: lista łańcuchów

    Zwraca: łańcuch
    """
    current = t[0]
    count = 0
    res = []
    for x in t:
        if x == current:
            count += 1
        else:
            append(res, current, count)
            current = x
            count = 1
    append(res, current, count)
    return setrep(res)


def setrep(s):
    """Zwraca reprezentację łańcuchową zestawu łańcuchów typu.

    s: zestaw łańcuchów typu

    Zwraca: łańcuch
    """
    rep = ', '.join(s)
    if len(s) == 1:
        return rep
    else:
        return '(' + rep + ')'
    return 


def append(res, typestr, count):
    """Dodaje nowy element do listy łańcuchów typu.

    Modyfikuje res.

    res: lista łańcuchów typu
    typestr: nowy łańcuch typu
    count: liczba wystąpień nowego typu

    Zwraca: None
    """
    if count == 1:
        rep = typestr
    else:
        rep = '%d %s' % (count, typestr)
    res.append(rep)


if __name__ == '__main__':

    t = [1, 2, 3]
    print(structshape(t))

    t2 = [[1, 2], [3, 4], [5, 6]]
    print(structshape(t2))

    t3 = [1, 2, 3, 4.0, '5', '6', [7], [8], 9]
    print(structshape(t3))

    class Point:
        """trywialny typ obiektu"""

    t4 = [Point(), Point()]
    print(structshape(t4))

    s = set('abc')
    print(structshape(s))

    lt = zip(t, s)
    print(structshape(lt))

    d = dict(lt)        
    print(structshape(d))

    it = iter('abc')
    print(structshape(it))
