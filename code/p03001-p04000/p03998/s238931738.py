# coding: utf-8
import sys


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = None

    def set_cards(self, cards):
        self.cards = cards

    def has_no_cards(self):
        return self.cards == []

    def play_card(self):
        return self.cards.pop(0)


def main(argv=sys.argv):

    a = Player('A')
    a.set_cards(list(input()))
    b = Player('B')
    b.set_cards(list(input()))
    c = Player('C')
    c.set_cards(list(input()))

    next_player = a
    while True:
        card = next_player.play_card()
        if card == 'a':
            next_player = a
        elif card == 'b':
            next_player = b
        elif card == 'c':
            next_player = c

        if next_player.has_no_cards():
            print(next_player.name)
            break

    return 0


if __name__ == '__main__':
    sys.exit(main())
