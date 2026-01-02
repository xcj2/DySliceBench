from typing import List, NamedTuple


class Card(NamedTuple):
    suit: str
    value: int


def bubble_sort(cards: List[Card]):
    for i in range(len(cards)):
        for j in range(len(cards) - 1, i, -1):
            if cards[j].value < cards[j - 1].value:
                cards[j], cards[j - 1] = cards[j - 1], cards[j]


def selection_sort(cards: List[Card]):
    for i in range(len(cards)):
        minj = i
        for j in range(i, len(cards)):
            if cards[j].value < cards[minj].value:
                minj = j
        cards[i], cards[minj] = cards[minj], cards[i]


def gen_numbet_card_pair(cards: List[Card]):
    return {n: [c for c in cards if c.value == n] for n in range(1, 10)}


def is_stable(in_cards: List[Card], out_cards: List[Card]):
    in_lists = gen_numbet_card_pair(in_cards)
    out_lists = gen_numbet_card_pair(out_cards)
    for n in range(10):
        if in_lists.get(n, []) != out_lists.get(n, []):
            return False
    return True


def printing(arr, f):
    b_arr = arr.copy()
    f(b_arr)
    print(" ".join([c.suit+str(c.value) for c in b_arr]))
    print("Stable" if is_stable(arr, b_arr) else "Not stable")


n = int(input())
cards: List[Card] = [Card(suit=x[0], value=int(x[1])) for x in input().split(" ")]
printing(cards, bubble_sort)
printing(cards, selection_sort)

