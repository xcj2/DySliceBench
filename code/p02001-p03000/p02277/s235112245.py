import sys


def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return i+1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


def isStable(A):
    for i in range(0, len(A)-1):
        if A[i][1] == A[i+1][1]:
            if A[i][2] > A[i+1][2]:
                return False
    return True

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    B = []
    for i in range(n):
        c = sys.stdin.readline().split()
        B.append([c[0], int(c[1]), i])
    quickSort(B, 0, n-1)
    if isStable(B):
        print("Stable")
    else:
        print("Not stable")
    for b in B:
        print(b[0], b[1])