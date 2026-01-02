if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    MAX = 100000
    SENTINEL = 2000000000

    class Card():
        def __init__(self, suit, value):
            self.suit = suit
            self.value = value

    def merge(A, n ,left, mid, right):
        n1 = mid - left
        n2 = right - mid
        L = [Card(None, None) for _ in range(n1+1)]
        R = [Card(None, None) for _ in range(n2+1)]
        for i in range(n1):
            L[i] = A[left + i]
        for i in range(n2):
            R[i] = A[mid + i]
        L[n1].value = SENTINEL
        R[n2].value = SENTINEL
        i, j = 0, 0
        for k in range(left, right):
            if L[i].value <= R[j].value:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1


    def mergeSort(A, n, left, right):
        if left+1 < right:
            mid = (left + right)//2
            mergeSort(A, n, left, mid)
            mergeSort(A, n, mid, right)
            merge(A, n, left, mid, right)


    def swap(a, i, j):
        # list aのi番目の要素とj番目の要素を交換する関数
        k = a[j]
        a[j] = a[i]
        a[i] = k

    def partition(A, p, r):
        x = A[r]
        i = p-1
        for j in range(p, r):
            if A[j].value <= x.value:
                i += 1
                swap(A, i, j)
        swap(A, i+1, r)
        return i+1

    def quickSort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            quickSort(A, p, q-1)
            quickSort(A, q+1, r)


    n = int(input())

    A = [Card(None, None) for _ in range(n)]
    B = [Card(None, None) for _ in range(n)]

    for i in range(n):
        suit, value = input().split()
        A[i].suit = suit
        B[i].suit = suit
        A[i].value = int(value)
        B[i].value = int(value)

    mergeSort(A, n, 0, n)
    quickSort(B, 0, n-1)

    for i in range(n):
        if A[i].suit != B[i].suit:
            print('Not stable')
            break
    else:
        print('Stable')

    for b in B:
        print(b.suit, b.value)

