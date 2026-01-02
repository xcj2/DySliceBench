class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __eq__(self, ins):
        if not isinstance(ins, Card):
            return NotImplemented
        return self.suit == ins.suit and self.value == ins.value

def bubbleSort(C, N):
    for i in range(N):
        for j in range(n-1, i, -1):
            if C[j].value < C[j-1].value:
                C[j], C[j-1] = C[j-1], C[j]

def selectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[minj].value > C[j].value:
                minj = j
        C[i], C[minj] = C[minj], C[i]

def printCard(C, N):
    c = [C[i].suit + C[i].value for i in range(N)]
    print(' '.join(c))

def isStable(inc, outc, N):
    for i in range(N):
        for j in range(i+1, N):
            for a in range(N):
                for b in range(a+1, N):
                    if inc[i].value == inc[j].value and inc[i] == outc[b] and inc[j] == outc[a]:
                        return False
    return True


n = int(input())
input_cards = [Card(*c) for c in input().split()]
output_cards = input_cards.copy()
bubbleSort(output_cards, n)
printCard(output_cards, n)
if isStable(input_cards, output_cards, n):
    print('Stable')
else:
    print('Not stable')
output_cards = input_cards.copy()
selectionSort(output_cards, n)
printCard(output_cards, n)
if isStable(input_cards, output_cards, n):
    print('Stable')
else:
    print('Not stable')
