from math import inf


def merge(A, left, mid, right):
    global count

    L = A[left: mid]
    R = A[mid: right]

    L.append(inf)
    R.append(inf)

    i = 0
    j = 0

    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            count += mid - left - i


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = int((left + right) / 2)
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


def main():
    global count
    n = int(input())
    A = list(map(int, input().split()))

    merge_sort(A, 0, n)
    print(count)


if __name__ == "__main__":
    count = 0
    main()

