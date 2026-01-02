def num(card):
    return int(card[2:])

def partition(A, p, r):
    x = num(A[r])
    i = p - 1
    for j in range(p, r):
        if num(A[j]) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

n = int(input())
A = [input() for _ in range(n)]
B = sorted(A, key=num)
quicksort(A, 0, n - 1)

msg = "Stable"
for i in range(n):
    if A[i] != B[i]:
        msg = "Not stable"
        break

print(msg)
for card in A:
    print(card)