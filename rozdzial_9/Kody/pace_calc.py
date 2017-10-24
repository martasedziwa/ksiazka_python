"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


"""

Jeśli 10-kilometrowy wyścig trwał 43 minuty i 30 sekund, jaki jest średni
czas przypadający na milę? Jaka jest średnia prędkość wyrażona w milach na
godzinę? Wskazówka: mila to 1,61 kilometra.

"""

minutes = 43.5
hours = minutes / 60

km_per_mile = 1.61
km = 10
miles = km / km_per_mile 

pace = minutes / miles
mph = miles / hours

print('Tempo w minutach na milę:', pace)
print('Średnia prędkość w milach/h:', mph)
