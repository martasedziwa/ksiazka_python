"""Moduł zawiera przykładowy kod powiązany z książką:

Myśl w języku Python! Wydanie drugie
Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

Licencja: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import random


class Card:
    """Reprezentuje standardową grę w karty.
    
    Atrybuty:
      suit: liczby całkowite 0-3
      rank: liczby całkowite 1-13
    """

    suit_names = ['trefl', 'karo', 'kier', 'pik']
    rank_names = [Brak, 'As', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Walet', 'Dama', 'Król']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Zwraca czytelną dla użytkownika reprezentację łańcuchową."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __eq__(self, other):
        """Sprawdza, czy self i other mają identyczną rangę i kolor.

        Zwraca: boolean
        """
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        """Porównuje daną kartę z inną najpierw według koloru, a następnie rangi.

        Zwraca: boolean
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """Reprezentuje talię kart.

    Atrybuty:
      cards: lista obiektów Card.
    """
    
    def __init__(self):
        """Inicjuje talię z 52 kartami.
        """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Zwraca reprezentację łańcuchową talii.
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Dodaje kartę do talii.

        card: Card
        """
        self.cards.append(card)

    def remove_card(self, card):
        """Usuwa kartę z talii lub zgłasza wyjątek, jeśli karty w niej nie ma.
        
        card: Card
        """
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Usuwa i zwraca kartę z talii.

        i: indeks karty do zwrócenia; domyślnie jest to ostatnia karta.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Przenosi karty w talii."""
        random.shuffle(self.cards)

    def sort(self):
        """Sortuje karty w kolejności rosnącej."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Przenosi daną liczbę kart z talii do dłoni.

        hand: docelowy obiekt Hand
        num: całkowita liczba kart do przeniesienia
        """
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Reprezentuje rozdanie kart do gry."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """Znajduje i zwraca obiekt klasy, który zapewni 
    definicję metody (jako łańcuch), jeśli wywoływana jest
    w obiekcie obj.

    obj: dowolny obiekt języka Python
    method_name: nazwa metody łańcuchowej
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)
