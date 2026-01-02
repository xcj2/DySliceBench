class card:
    def __init__(self, suit, value, no):
        self.suit = suit
        self.value = value
        self.no = no
def partition(A, p, r):
    piv = A[r].value
    i = p - 1
    for j in range(p, r):
        if A[j].value <= piv:
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q, r)

def isstable(A, n):
    for i in range(n-1):
        if A[i].value == A[i+1].value and A[i].no > A[i+1].no:
            print("Not stable")
            return
    print("Stable")


n = int(input())
cards=[]

for i in range(n):
    temp = list(input().split())
    ob = card(temp[0], int(temp[1]), i)
    cards.append(ob)
quicksort(cards, 0, n-1)
isstable(cards, n)
for i in range(n):
    print(cards[i].suit + " " + str(cards[i].value))
