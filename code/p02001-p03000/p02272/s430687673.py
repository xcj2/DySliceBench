counter = 0


def merge(A, left, mid, right):
    m = mid - left
    n = right - mid
    L = [None] * (m+1)
    R = [None] * (n+2)

    for i in range(m):
        L[i] = A[left + i]

    for i in range(n):
        R[i] = A[mid + i]

    L[m], R[n] = float("inf"), float("inf")  # stoper
    i, j = 0, 0

    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    global counter
    counter += right - left
    return


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)
    return A


def main():
    _ = input()
    A = [int(i) for i in input().strip().split()]
    merge_sort(A, 0, len(A))
    print(" ".join([str(i) for i in A]))


if __name__ == "__main__":
    counter = 0
    main()
    print(counter)

