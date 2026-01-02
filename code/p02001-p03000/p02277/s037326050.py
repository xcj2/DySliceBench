def num(card):
    return int(card[0][2:])

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

def is_stable(A):
    for i in range(n - 1):
        if num(A[i]) == num(A[i + 1]) and A[i][1] > A[i + 1][1]:
            return False
    return True

n = int(input())
A = [(input(), i) for i in range(n)]
quicksort(A, 0, n - 1)

print("Stable" if is_stable(A) else "Not stable")
for card in A:
    print(card[0])