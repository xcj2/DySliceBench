def merge(A, left, mid, right):
    count = 0
    L = A[left:mid]
    R = A[mid:right]
    L.append(1000000001)
    R.append(1000000001)
    i, j = 0, 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            if L[i] != 1000000001:
                count += mid + j - k - 1
    return count


def mergesort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        countL = mergesort(A, left, mid)
        countR = mergesort(A, mid, right)
        return merge(A, left, mid, right) + countL + countR
    return 0


def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = mergesort(A, 0, n)
    print(ans)


if __name__ == '__main__':
    main()
