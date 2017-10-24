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
        # Problem dotyczy wartości domyślnej zawartości.
        # Wartości domyślne są określane RAZ w momencie
        # definiowania funkcji. Wartości nie są określane
        # ponownie w momencie wywoływania funkcji.
        
        # W tym przypadku oznacza to, że w momencie zdefiniowania
        # __init__ określana jest wartość [], a zawartość
        # uzyskuje odwołanie do pustej listy.
        
        # Później każdy obiekt Kangaroo uzyskujący wartość
        # domyślną otrzymuje odwołanie do TEJ SAMEJ listy.
        # Jeśli taka współużytkowana lista zostanie zmodyfikowana
        # przez dowolny obiekt Kangaroo, zmiana widoczna jest
        # dla wszystkich obiektów.
        
        # Następna wersja __init__ prezentuje idiomatyczny
        # sposób uniknięcia tego problemu.
        self.name = name
        self.pouch_contents = contents

    def __init__(self, name, contents=None):
        """Inicjowanie zawartości torby.

        name: string
        contents: początkowa zawartość torby.
        """
        # W tej wersji wartość domyślna to None. Po uruchomieniu
        # __init__ sprawdza wartość zawartości, i w razie potrzeby,
        # tworzy nową, pustą listę. Dzięki temu każdy obiekt
        # Kangaroo uzyskujący wartość domyślną otrzymuje
        # odwołanie do innej listy.
        
        # Zgodnie z ogólną zasadą należy unikać używania obiektu
        # zmiennego jako wartości domyślnej, chyba że naprawdę
        # wiesz, co robisz.
        self.name = name
        if contents == None:
            contents = []
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
print(roo)

# Jeśli program zostanie uruchomiony w takie postaci, powinien działać.
# Aby zlokalizować problem, spróbuj wyświetlić roo.
