import math

def partition(A, p, r):
    x = int(A[r][2:])
    i = p-1
    for j in range(p, r):
        if int(A[j][2:]) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [None for _ in range(n1+1)]
    R = [None for _ in range(n2+1)]
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]

    L[n1] = math.inf
    R[n2] = math.inf

    i = 0
    j = 0

    for k in range(left, right):
        try:
            v1 = int(L[i][2:])
        except:
            v1 = L[i]

        try:
            v2 = int(R[j][2:])
        except:
            v2 = R[j]

        if v1 <= v2:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

    return A


if __name__ == "__main__":
    n = int(input())
    cards = []
    for i in range(n):
        cards.append(input())

    reference = merge_sort(cards.copy(), 0, n)
    quicksort(cards, 0, n-1)

    if cards == reference:
        print('Stable')
    else:
        print('Not stable')

    for card in cards:
        print(card)


