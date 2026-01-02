def show(A, n):
    for i in range(n):
        if i != n-1:
            print(A[i], end=' ')
        else:
            print(A[i])


def selection_sort(A, n):
    count = 0
    for i in range(n-1):
        min_j = i
        for j in range(i+1, n):
            if A[min_j] > A[j]:
                min_j = j
        if min_j != i:
            A[i], A[min_j] = A[min_j], A[i]
            count += 1
    show(A, n)
    print(count)


def main():
    n = int(input())
    A = list(map(int, input().split()))
    selection_sort(A, n)


if __name__ == "__main__":
    main()

