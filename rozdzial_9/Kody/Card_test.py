"""Plik zawiera kod używany w wypadku książki Think Stats,
 Allena B. Downey'a, która dostępna jest w witrynie o adresie greenteapress.com

Copyright 2014 Allen B. Downey
Licencja: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import unittest
from Card import Card, Deck


class Test(unittest.TestCase):

    def testDeckRemove(self):
        deck = Deck()
        card23 = Card(2, 3)
        deck.remove_card(card23)


if __name__ == "__main__":
    unittest.main()
