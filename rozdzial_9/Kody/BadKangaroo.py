"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

"""

OSTRZEŻENIE: program zawiera NIEMIŁY błąd. Wstawiam go
celowo jako ćwiczenie z debugowania, ale
emulowanie tego przykładu NIE JEST WYMAGANE!

"""

class Kangaroo:
    """Kangur to torbacz."""
    
    def __init__(self, name, contents=[]):
        """Inicjowanie zawartości torby.

        name: string
        contents: początkowa zawartość torby.
        """
        self.name = name
        self.pouch_contents = contents

    def __str__(self):
        """Zwraca reprezentację łańcuchową danego obiektu Kangaroo.
        """
        t = [ ' Zawartość torby dla:' + self.name ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Dodaje nowy obiekt do zawartości torby.

        item: obiekt do dodania
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)

# Jeśli program zostanie uruchomiony w takie postaci, powinien działać.
# Aby zlokalizować problem, spróbuj wyświetlić roo.

# Wskazówka: w celu zlokalizowania problemu spróbuj uruchomić pylint.
