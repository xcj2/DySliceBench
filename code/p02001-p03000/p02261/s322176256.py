from copy import copy
from collections import defaultdict  

def bubble_sort(collection):
    collection = copy(collection)
    for i in range(len(collection)):
        for j in range(len(collection)-1, i, -1):
            if collection[j] < collection[j-1]:
                collection[j], collection[j-1] = collection[j-1], collection[j]
    return collection
    
def selection_sort(collection):
    collection = copy(collection)
    for i in range(len(collection)):
        mini = i
        for j in range(i, len(collection)):
            if collection[j] < collection[mini]:
                mini = j
        collection[i], collection[mini] = collection[mini], collection[i]
        
    return collection
    
def print_cards(cards):
    for card in cards[:-1]:
        print(card, end=' ')
    print(cards[-1])

def find_card_order(cards):
    duplicate_numbers = defaultdict(list)
    for card in cards:
        duplicate_numbers[card.number].append(card.suit)
    duplicate_numbers = {k: v for k, v in duplicate_numbers.items() if len(v) >= 2}
    return duplicate_numbers



class Card:
    def __init__(self, card):
        self._suit = card[0]
        self._number = int(card[1])
    
    def __str__(self):
        return self.card
    
    def __lt__(self, other):
        return self._number < other._number
        
    @property
    def card(self):
        return self._suit + str(self._number)
    
    @property
    def number(self):
        return self._number
    @property
    def suit(self):
        return self._suit
        
nums_card = int(input())
cards = list(map(Card, input().split()))
duplicate_cards =  find_card_order(cards)
bubble_sorted = bubble_sort(cards)
selection_sorted = selection_sort(cards)


print_cards(bubble_sorted)

stable = 'Stable'
for k, v in duplicate_cards.items():
    sorted_order = [card.suit for card in bubble_sorted if card.number == k]
    if duplicate_cards[k] != sorted_order:
        stable = 'Not stable'
print(stable)

print_cards(selection_sorted)
stable = 'Stable'
for k, v in duplicate_cards.items():
    sorted_order = [card.suit for card in selection_sorted if card.number == k]
    if duplicate_cards[k] != sorted_order:
        stable = 'Not stable'
print(stable)
