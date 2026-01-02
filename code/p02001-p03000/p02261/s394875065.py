def bubbleSort(a,n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if a[j-1][1] > a[j][1]: #Sort by card number
                a[j-1], a[j] = a[j], a[j-1]
    print(' '.join(a))

def selectionSort(a,n):
    for i in range(n):
        minj = i
        for j in range(i,n):
            if a[j][1] < a[minj][1]: #Sort by card number
                minj = j
        if minj != i:
            a[i],a[minj] = a[minj],a[i]
    a = [str(s) for s in a]
    print(' '.join(a))

def isStable(a, a2):
    """
    :param a: Stable-sorted list (Bubble sort)
    :param a2: List to check if isStable
    :return: Boolean
    """
    if a == a2:
        return True
    else:
        return False

n = int(input())
a = list(input().split())
a2 = a[::]

bubbleSort(a,n)
print('Stable')
selectionSort(a2,n)
print('Stable' if isStable(a, a2) else 'Not stable')
