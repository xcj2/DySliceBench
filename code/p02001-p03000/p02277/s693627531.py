def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def main():
    n = int(input())
    A = []
    for i in range(n):
        m, s = input().split()
        s = int(s)
        A.append([m, s])
    B = A[:]
    quicksort(B, 0, n-1)

    for i in range(n-1):
        if B[i][1] == B[i + 1][1]:
            if A.index(B[i]) > A.index(B[i + 1]):
                print("Not stable")
                break
    else:
        print("Stable")

    for i in range(n):
        print(*B[i])


if __name__ == '__main__':
    main()

