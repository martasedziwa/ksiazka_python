"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import os


def walk(dirname):
    """Znajduje nazwy wszystkich plików w katalogu dirname i jego podkatalogach.

    dirname: nazwa katalogu w postaci łańcucha
    """
    names = []
    if '__pycache__' in dirname:
        return names

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    """Oblicza sumę kontrolną MD5 zawartości pliku.

    filename: string
    """
    cmd = 'md5sum ' + filename
    return pipe(cmd)


def check_diff(name1, name2):
    """Określa różnicę między zawartością dwóch plików.

    name1, name2: nazwy plików w postaci łańcucha
    """
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)


def pipe(cmd):
    """Uruchamia polecenie w procesie podrzędnym.

    cmd: łańcuchowe polecenie systemu Unix

    Zwraca (res, stat): dane wyjściowe procesu podrzędnego i status wyjścia.
    """
    # Uwaga: metoda os.popen jest obecnie wycofywana, co oznacza, że
    # należy zakończyć korzystanie z niej i zacząć używać
    # modułu procesu podrzędnego. Jednakże w prostych przypadkach proces podrzędny
    # uważam za bardziej złożony niż jest to wymagane. Z tego powodu
    # będę używać metody os.popen do momentu, aż przestanie być dostępna.

    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    """Oblicza sumy kontrolne dla wszystkich plików z danym przyrostkiem.

    dirname: nazwa katalogu w postaci łańcucha do wyszukania
    suffix: przyrostek w postaci łańcucha do dopasowania

    Zwraca: odwzorowanie sumy kontrolnej na listę plików z tą sumą
    """
    names = walk(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    """Sprawdza, czy dowolny plik na liście różni się od pozostałych.

    names: lista nazw plików w postaci łańcucha
    """
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    """Sprawdza zduplikowane pliki.

    Zgłasza wszystkie pliki z identyczną sumę kontrolną i sprawdza, czy
    faktycznie są jednakowe.

    d: odwzorowanie sumy kontrolnej na listę plików z tą sumą
    """
    for key, names in d.items():
        if len(names) > 1:
            print('Następujące pliki mają identyczną sumę kontrolną:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('I są jednakowe.')


if __name__ == '__main__':
    d = compute_checksums(dirname='.', suffix='.py')
    print_duplicates(d)
