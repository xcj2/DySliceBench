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

def is_stable(A, B):
    C = B[:]
    for card in A:
        i = C.index(card)
        if i == 0:
            pass
        elif num(C[i - 1]) == num(card):
            return False
        del C[i]
    return True

n = int(input())
A = [input() for _ in range(n)]
B = A[:]
quicksort(B, 0, n - 1)

print("Stable" if is_stable(A, B) else "Not stable")
for card in B:
    print(card)