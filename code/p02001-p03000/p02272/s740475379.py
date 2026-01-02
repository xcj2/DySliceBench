SENTINEL = float('inf')
count = 0


def main():
    n = int(input())
    a_s = list(map(int, input().split(' ')))
    merge_sort(a_s, n, 0, n)
    print(' '.join(map(str, a_s)))
    print(count)


def merge_sort(A, n, left, right):
    if left+1 < right:
        mid = (left+right) // 2
        merge_sort(A, n, left, mid)
        merge_sort(A, n, mid, right)
        merge(A, n, left, mid, right)


def merge(A, n, left, mid, right):
    global count
    L = A[left:mid]
    R = A[mid:right]
    L.append(SENTINEL)
    R.append(SENTINEL)
    i = j = 0
    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


if __name__ == "__main__":
    main()

