def bubble_sort(cards, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if cards[j][1] < cards[j-1][1]:
                cards[j], cards[j-1] = cards[j-1], cards[j]

    return cards

def selection_sort(cards, n):
    for i in range(n):
        minj = i

        for j in range(i, n):
            if cards[j][1] < cards[minj][1]:
                minj = j

        if i != minj:
            cards[i], cards[minj] = cards[minj], cards[i]

    return cards

def is_stable(cards, sorted_cards):
    hashed = {}

    for m, v in cards:
        if v not in hashed:
            hashed[v] = []

        hashed[v].append((m, v))

    for sm, sv in sorted_cards:
        if hashed[sv][0] != (sm, sv):
            return False

        hashed[sv] = hashed[sv][1:]

    return True

def print_cards(cards, sorted_cards):
    print(' '.join([card[0]+str(card[1]) for card in sorted_cards]))

    if is_stable(cards, sorted_cards):
        print('Stable')
    else:
        print('Not stable')

def main():
    n = int(input())
    cards = [(card[0], int(card[1])) for card in input().split()]

    sorted_cards = bubble_sort(cards[:], n)
    print_cards(cards, sorted_cards)

    sorted_cards = selection_sort(cards[:], n)
    print_cards(cards, sorted_cards)

if __name__ == '__main__':
    main()

