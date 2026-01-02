def partition(A, p, r):
    x = A[r][1]
    i = p - 1

    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def main():
    n = int(input())
    A = []

    for i in range(n):
        mark, num = input().split()
        A.append([mark, int(num), i])

    quick_sort(A, 0, n - 1)

    flag = False
    for i in range(1, n):
        if A[i - 1][1] == A[i][1]:
            if A[i - 1][2] > A[i][2]:
                flag = True
                break

    if flag:
        print("Not stable")
    else:
        print("Stable")

    for i in range(n):
        print(A[i][0], A[i][1])


if __name__ == "__main__":
    main()

