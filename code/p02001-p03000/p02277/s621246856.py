class Card:
    def __init__(self):
        self.suit = ''
        self.value = 0

def partition(A, p, r):
    x = A[r].value
    i = p
    for j in range(p, r):
        if A[j].value <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

def quickSort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def main():
    n = int(input())
    A = []
    for _ in range(n):
        card = Card()
        _input = input().split(" ")
        card.suit = _input[0]
        card.value = int(_input[1])
        A.append(card)
    
    ind = dict((e, i) for i, e in enumerate(A))
    quickSort(A, 0, n-1)
    
    for i in range(n - 1):
        if A[i].value == A[i + 1].value:
            if ind[A[i]] > ind[A[i + 1]]:
                print('Not stable')
                break
    else:
        print('Stable')
    
    for i in range(n):
        print(A[i].suit, A[i].value)
             
if __name__ == "__main__":
    main()
