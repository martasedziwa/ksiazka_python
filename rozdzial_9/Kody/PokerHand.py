  """Moduł zawiera przykładowy kod powiązany z książką:

  Myśl w języku Python! Wydanie drugie
  Allen Downey
  http://thinkpython2.com

  Copyright 2015 Allen Downey

  Licencja: http://creativecommons.org/licenses/by/4.0/
  """

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Reprezentuje rozdanie pokerzysty."""

    def suit_hist(self):
        """Buduje histogram kolorów pojawiających się w rozdaniu.

        Przechowuje wynik w atrybucie suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Zwraca wartość True, jeśli rozdanie zawiera kolor. W przeciwnym razie jest to wartość False.
      
        Zauważ, że działa to poprawnie w wypadku rozdań liczących więcej niż 5 kart.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


if __name__ == '__main__':
    # utworzenie talii
    deck = Deck()
    deck.shuffle()

    # obsługa kart i klasyfikowanie rozdań
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.has_flush())
        print('')

