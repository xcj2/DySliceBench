def bubble_sort(A, n):
    A = A[:]
    flag = True
    while flag:
        flag = False
        for i in range(n - 1, 0, -1):
            if int(A[i][1:]) < int(A[i - 1][1:]):
                A[i], A[i - 1] = A[i - 1], A[i]
                flag = True
    return A


def selection_sort(A, n):
    A = A[:]
    for start in range(n):
        smallest_i = start
        smallest = A[smallest_i]
        for i in range(start, n):
            if int(A[i][1:]) < int(smallest[1:]):
                smallest_i = i
                smallest = A[smallest_i]
        A[start], A[smallest_i] = A[smallest_i], A[start]
    return A


def is_stable(ordered, original):
    for n in range(1, 10):
        f_original = filter(lambda c: int(c[1:]) == n, original)
        f_ordered = filter(lambda c: int(c[1:]) == n, ordered)
        for a, b in zip(f_ordered, f_original):
            if a != b:
                return False
    return True


n = int(input())
A = input().split()
bA = bubble_sort(A, n)
sA = selection_sort(A, n)
print(*bA, sep=" ")
print("Stable" if is_stable(bA, A) else "Not stable")
print(*sA, sep=" ")
print("Stable" if is_stable(sA, A) else "Not stable")

