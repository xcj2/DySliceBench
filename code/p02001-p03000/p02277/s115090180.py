def partition(A, p, r):
    x = A[r][2]
    i = p - 1

    for j in range(p, r):
        if A[j][2] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def IsStable(A):
    for index, a in enumerate(A):
        for i in range(index, len(A)):
            if (a[2] == A[i][2]) and (a[0] > A[i][0]):
                return "Not stable"

    return "Stable"



n = int(input())
A = []
for i in range(n):
    a, b = input().split()
    A.append([i, a, int(b)])

quickSort(A, 0, len(A) - 1)

print(IsStable(A))
[print("{} {}".format(A[i][1], A[i][2])) for i in range(len(A))]
