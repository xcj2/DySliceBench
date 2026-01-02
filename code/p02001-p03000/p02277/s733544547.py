import sys

sys.setrecursionlimit(10**6)


def partition(A, p, r):

    x = A[r][1]
    i = p - 1

    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def main():

    N = int(sys.stdin.readline().rstrip())

    A = []

    for i in range(N):
        m, n = sys.stdin.readline().rstrip().split()
        A.append((m, int(n), i))  # stable 確認用に index をつけておく

    quicksort(A, 0, N - 1)

    for i in range(1, N):
        if A[i][1] == A[i - 1][1]:
            if A[i][2] < A[i - 1][2]:
                print("Not stable")
                break
    else:
        print("Stable")

    for m, n, _ in A:
        print(m, n)


main()

