#!usr/bin/env python3

import sys


def init_card_deck():
    # S: spades
    # H: hearts
    # C: clubs
    # D: diamonds
    card_deck = {'S': [], 'H': [], 'C': [], 'D': []}
    n = int(sys.stdin.readline())

    for i in range(n):
        lst = [card for card in sys.stdin.readline().split()]
        card_deck[lst[0]].append(lst[1])

    return card_deck


def print_missing_cards(card_deck):
    card_symbols = ['S', 'H', 'C', 'D']

    for i in card_symbols:
        for card in range(1, 14):
            if not str(card) in card_deck[i]:
                print(i, card)


def main():
    print_missing_cards(init_card_deck())


if __name__ == '__main__':
    main()