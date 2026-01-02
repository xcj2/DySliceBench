def partition(a, p, r):
    x = a[r][1]
    i = p-1

    for j in range(p, r):
        if a[j][1] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i+1], a[r] = a[r], a[i+1]
    return i+1


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)


def isstable(a):
    for i in range(n-1):
        if a[i][1] == a[i+1][1]:
            if a[i][2] > a[i+1][2]:
                return False
    return True


n = int(input())
deck = [None]*n
for num in range(n):
    card = input().split()
    deck[num] = [card[0], int(card[1]), num]

quicksort(deck, 0, n-1)
if isstable(deck):
    print("Stable")
else:
    print("Not stable")
[print(deck[i][0], deck[i][1]) for i in range(n)]