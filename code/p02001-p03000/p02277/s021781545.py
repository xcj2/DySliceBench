class card():
    def __init__(self, suit, number):
        self.s = suit
        self.n = number

def Partition(A, p, r):
    x = int(A[r].n)
    i = p - 1

    for j in range(p, r):
        if int(A[j].n) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1

def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)

def Main():

    n = int(input())
    cards = list()
    
    for i in range(n):
        S, N = input().split()
        c = card(S, N)
        cards.append(c)

    reference = sorted(cards, key=lambda x: int(x.n))
    QuickSort(cards, 0, len(cards) - 1)

    flag = 1

    for i in range(len(cards)):
        if cards[i].s != reference[i].s or cards[i].n != reference[i].n :
            flag = 0
            break;
    
    if flag:
        print("Stable")
    else:
        print("Not stable")

    for i in range(len(cards)):
        print("{0} {1}".format(cards[i].s, cards[i].n))
        
Main()
