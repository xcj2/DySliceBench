def partition(A, p, r):
    x = A[r][1]
    i = p-1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            memo = A[i]
            A[i] = A[j]
            A[j] = memo
    memo = A[i+1]
    A[i+1] = A[r]
    A[r] = memo
    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


n = int(input())
card = []
for i in range(n):
    word, num = input().split()
    card.append([word, int(num), int(i)])

def checkstable(card):
    for i in range(len(card) - 1):
        if card[i][1] == card[i + 1][1] and card[i][2] > card[i+1][2]:
            return "Not stable"
    return "Stable"

quicksort(card, 0, n-1)

print(checkstable(card))
for c in card:
    print(c[0], c[1])
