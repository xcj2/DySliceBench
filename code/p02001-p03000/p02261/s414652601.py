class Card:
    def __init__(self, name):
        self.name = name
        self.value = int(name[1])
    def __lt__(self, other):
        return self.value < other.value
    def __repr__(self):
        return self.name

def bubble_sort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j] < C[j-1]:
                C[j], C[j-1] = C[j-1], C[j]
    return C

def selection_sort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j] < C[minj]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

n = int(input())
cards = [Card(s) for s in input().split()]

bubbled_cards = bubble_sort(cards[:], n)
selected_cards = selection_sort(cards[:], n)
print(' '.join(str(s) for s in bubbled_cards))
print('Stable')
print(' '.join(str(s) for s in selected_cards))
if bubbled_cards == selected_cards:
    print('Stable')
else:
    print('Not stable')