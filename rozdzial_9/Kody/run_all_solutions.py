"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import os


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


filenames = """
ackermann_memo.py        grid.py             PokerHand.py
ackermann.py             has_duplicates.py   PokerHandSoln.py
anagram_db.py            header.py           polygon.py
anagram_sets.py          inlist.py           reducible.py
analyze_book1.py         interlock.py        reverse_pair.py
analyze_book2.py         invert_dict.py      rotate_pairs.py
analyze_book3.py         koch.py             rotate.py
BadKangaroo.py           letters.py          sed.py
birthday.py              Map.py              spiral.py
Card.py                  markov.py           structshape.py
cartalk1.py              Markov.py           Time1.py
cartalk2.py              metathesis.py       Time1_soln.py
cartalk3.py              most_frequent.py    Time2.py
do_four.py               pace_calc.py        Time2_soln.py
                         palindrome_soln.py  typewriter.py
find_duplicates_copy.py  pie.py              unstable_sort.py
find_duplicates.py       pi.py               walk.py
flower.py                Point1.py           wordlist.py
GoodKangaroo.py          Point1_soln.py      zipf.py
"""

slow_ones = """
spiral.py                typewriter.py       pie.py
flower.py                wordlist.py         polygon.py
koch.py                  letters.py          zipf.py
""".split()


for filename in filenames.split():
    print(filename)
    if filename in slow_ones:
        print('Pomijanie')
        continue

    res, stat = pipe('python ' + filename)
    print(stat)

