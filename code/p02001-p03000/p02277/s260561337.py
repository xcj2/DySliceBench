def partition(A, p, r):
    x = int(A[r][1])
    i = p-1
    for j in range(p, r):
        if int(A[j][1]) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def is_stable(cards):
    for i in range(1, len(cards)):
        if cards[i-1][1] == cards[i][1]:
            if cards[i-1][2] > cards[i][2]:
                return False
    return True


n = int(input())
cards = []
for i in range(n):
    cards.append(input().split() + [i])
quicksort(cards, 0, n - 1)
print("Stable" if is_stable(cards) else "Not stable")
for card in cards:
    print(card[0], card[1])