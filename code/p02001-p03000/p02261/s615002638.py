"""ALDS1_2_C"""

from collections import namedtuple
from copy import deepcopy

Card = namedtuple("Card", ("suit", "value"))

def bubble(cards):
    cards = deepcopy(cards)
    N = len(cards)
    for i in range(N):
        for j in range(N-1, i, -1):
            if cards[j].value < cards[j-1].value:
                cards[j], cards[j-1] = cards[j-1], cards[j]
    return cards


def selection(cards):
    cards = deepcopy(cards)
    N = len(cards)
    for i in range(N):
        argmin = i
        for j in range(i, N):
            if cards[j].value < cards[argmin].value:
                argmin = j
        cards[i], cards[argmin] = cards[argmin], cards[i]
    return cards


def print_cards(cards):
    for i, card in enumerate(cards):
        end = "" if i == len(cards) - 1 else " "
        print(card.suit, card.value, sep="", end=end)
    print()


def main():
    _ = input()
    cards = [Card(i[0], int(i[1])) for i in input().split()]
    bubble_sorted = bubble(cards)
    selection_sorted = selection(cards)

    print_cards(bubble_sorted)
    print("Stable")
    print_cards(selection_sorted)
    if bubble_sorted == selection_sorted:
        print("Stable")
    else:
        print("Not stable")


if __name__ == "__main__":
    main()
