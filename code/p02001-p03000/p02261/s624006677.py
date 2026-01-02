from collections import namedtuple


Card = namedtuple('Card', 'suit value')
Card.__str__ = lambda self: self.suit + str(self.value)


def printcards(cards):
    print(' '.join([str(c) for c in cards]))


def bubblesort(it, key):
    it = list(it)
    for start_ind in range(len(it)):
        for target_ind in range(len(it)-1, start_ind, -1):
            target_val = key(it[target_ind])
            compare_val = key(it[target_ind-1])
            if target_val < compare_val:
                it[target_ind], it[target_ind-1] = it[target_ind-1], it[target_ind],
    return it


def selectsort(it, key):
    it = list(it)
    for start_ind in range(len(it)):
        min_ind = start_ind
        for target_ind in range(start_ind, len(it)):
            target_val = key(it[target_ind])
            min_val = key(it[min_ind])
            if target_val < min_val:
                min_ind = target_ind
        it[start_ind], it[min_ind] = it[min_ind], it[start_ind]
    return it


if __name__ == '__main__':
    n = int(input())
    cards = [Card(*suit_val) for suit_val in input().split()]
    cards_bub = bubblesort(cards, key=lambda x: x.value)
    cards_slc = selectsort(cards, key=lambda x: x.value)
    printcards(cards_bub)
    print('Stable')
    printcards(cards_slc)
    print('Stable') if cards_bub == cards_slc else print('Not stable')

