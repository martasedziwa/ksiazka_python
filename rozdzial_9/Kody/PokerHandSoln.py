"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class Hist(dict):
    """Odwzorowanie każdego elementu (x) na jego częstość."""

    def __init__(self, seq=[]):
        "Tworzy nowy histogram, rozpoczynając od elementów w seq."
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        "Inkrementuje (lub dekrementuje) licznik powiązany z elementem x."
        self[x] = self.get(x, 0) + f
        if self[x] == 0:
            del self[x]


class PokerHand(Hand):
    """Reprezentuje rozdanie pokerzysty."""

    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def make_histograms(self):
        """Oblicza histogramy dla kolorów i rozdań.

        Tworzy atrybuty:

          suits: histogram kolorów w rozdaniu.
          ranks: histogram rang.
          sets: posortowana lista zestawów rang w rozdaniu.
        """
        self.suits = Hist()
        self.ranks = Hist()
        
        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)

        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)
 
    def has_highcard(self):
        """Zwraca wartość True, jeśli dane rozdanie zawiera wysoką kartę."""
        return len(self.cards)
        
    def check_sets(self, *t):
        """Sprawdza, czy self.sets zawiera zestawy, które
        są co najmniej tak duże jak wymagania w t.

        t: lista liczb całkowitych
        """
        for need, have in zip(t, self.sets):
            if need > have:
                return False
        return True

    def has_pair(self):
        """Sprawdza, czy dane rozdanie zawiera parę."""
        return self.check_sets(2)
        
    def has_twopair(self):
        """Sprawdza, czy dane rozdanie zawiera dwie pary."""
        return self.check_sets(2, 2)
        
    def has_threekind(self):
        """Sprawdza, czy dane rozdanie zawiera trójkę."""
        return self.check_sets(3)
        
    def has_fourkind(self):
        """Sprawdza, czy dane rozdanie zawiera karetę."""
        return self.check_sets(4)

    def has_fullhouse(self):
        """Sprawdza, czy dane rozdanie zawiera fula."""
        return self.check_sets(3, 2)

    def has_flush(self):
        """Sprawdza, czy dane rozdanie zawiera kolor."""
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_straight(self):
        """Sprawdza, czy dane rozdanie zawiera strita."""
        # utworzenie kopii histogramu rang przed przetworzeniem go
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0)

        # sprawdzenie, czy uzyskano 5 pod rząd
        return self.in_a_row(ranks, 5)

    def in_a_row(self, ranks, n=5):
        """Sprawdza, czy histogram zawiera n rang pod rząd.

        hist: odwzorowanie rangi na częstość
        n: wymagana liczba docelowa
        """
        count = 0
        for i in range(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == n:
                    return True
            else:
                count = 0
        return False
    
    def has_straightflush(self):
        """Sprawdza, czy dane rozdanie zawiera pokera.

        Nieporęczny algorytm.
        """
        # utworzenie zestawu istniejących par (ranga, kolor)
        s = set()
        for c in self.cards:
            s.add((c.rank, c.suit))
            if c.rank == 1:
                s.add((14, c.suit))

        # iteracja dla kolorów i rang, a ponadto sprawdzenie możliwości
        # uzyskania 5 pod rząd
        for suit in range(4):
            count = 0
            for rank in range(1, 15):
                if (rank, suit) in s:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
        return False
                
    def has_straightflush(self):
        """Sprawdza, czy dane rozdanie zawiera pokera.

        Lepszy algorytm (w tym sensie, że jest w sposób bardziej oczywisty poprawny).
        """
        # przydzielenie rozdania według koloru i sprawdzenie każdego
        # dodatkowe rozdanie w wypadku strita
        d = {}
        for c in self.cards:
            d.setdefault(c.suit, PokerHand()).add_card(c)

        # sprawdzenie, czy dowolne z przydzielonych rozdań zawiera strita
        for hand in d.values():
            if len(hand.cards) < 5:
                continue            
            hand.make_histograms()
            if hand.has_straight():
                return True
        return False

    def classify(self):
        """Klasyfikuje dane rozdanie.

        Tworzy atrybuty:
          etykiety:
        """
        self.make_histograms()

        self.labels = []
        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.labels.append(label)


class PokerDeck(Deck):
    """Reprezentuje talię kart umożliwiającą rozdania pokerowe."""

    def deal_hands(self, num_cards=5, num_hands=10):
        """Obsługuje rozdania z talii i zwraca je.

        num_cards: liczba kart w rozdaniu
        num_hands: liczba rozdań

        Zwraca: lista rozdań
        """
        hands = []
        for i in range(num_hands):        
            hand = PokerHand()
            self.move_cards(hand, num_cards)
            hand.classify()
            hands.append(hand)
        return hands


def main():
    # histogram etykiet: odwzorowanie etykiety na liczbę wystąpień
    lhist = Hist()

    # wykonanie pętli n razy, obsługa 7 rozdań na iterację, z których każde zawiera 7 kart
    n = 10000
    for i in range(n):
        if i % 1000 == 0:
            print(i)
            
        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_hands(7, 7)
        for hand in hands:
            for label in hand.labels:
                lhist.count(label)
            
    # print the results
    total = 7.0 * n
    print(total, 'Liczba obsłużonych rozdań:')

    for label in PokerHand.all_labels:
        freq = lhist.get(label, 0)
        if freq == 0: 
            continue
        p = total / freq
        print('%s występuje raz w %.2f' % (label, p))

        
if __name__ == '__main__':
    main()

