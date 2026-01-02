class Card:
    def __init__(self, kind, number):
        self.kind = kind
        self.number = number

def bubble_sort(C, N):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if C[j].number < C[j -1].number:
                C[j], C[j - 1] = C[j - 1], C[j]
    return C

def selection_sort(C, N):
    for i in range(N):
        min_index = i
        for j in range(i, N):
            if C[j].number < C[min_index].number:
                min_index = j
        C[i], C[min_index] = C[min_index], C[i]
    return C

def check_stable(bubble_cards, selection_cards):
    res = 'Stable'
    for (b, s) in zip(bubble_cards, selection_cards):
        if b.kind != s.kind or b.number != s.number:
            res = 'Not stable'
    return res

n = int(input())
bubble_cards = []
for card in input().split():
    kind, number = list(card)
    bubble_cards.append(Card(kind, number))
selection_cards = bubble_cards[:]

bubble_cards = bubble_sort(bubble_cards, n)
ans = []
for c in bubble_cards:
    ans.append(''.join(c.kind + str(c.number)))
print(' '.join(ans))
print('Stable')

selection_cards = selection_sort(selection_cards, n)
ans = []
for c in selection_cards:
    ans.append(''.join(c.kind + str(c.number)))
print(' '.join(ans))
print(check_stable(bubble_cards, selection_cards))

