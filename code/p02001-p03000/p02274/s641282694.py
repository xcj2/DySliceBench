SENTINEL = float('inf')


def main():
    n = int(input())
    A = list(map(int, input().split(' ')))

    result = merge_sort(A, n, 0, n)
    print(result)


def bubble_sort(array, n):
    count = 0
    for i in range(n):
        for j in range(n-1, i, -1):
            if array[j] < array[j-1]:
                count += 1
                array[j], array[j-1] = array[j-1], array[j]
    return count


def merge_sort(A, n, left, right):
    if left+1 < right:
        mid = (left+right) // 2
        v1 = merge_sort(A, n, left, mid)
        v2 = merge_sort(A, n, mid, right)
        v3 = merge(A, n, left, mid, right)
        return v1+v2+v3
    return 0


def merge(A, n, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    L.append(SENTINEL)
    R.append(SENTINEL)
    i = j = 0
    count = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            count += mid + j - k - 1
    return count


if __name__ == '__main__':
    main()

