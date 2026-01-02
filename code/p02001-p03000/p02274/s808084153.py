def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    cnt = 0

    def merge(A, l, mid, r):
        nonlocal cnt
        n1 = mid - l
        n2 = r - mid
        L = [A[l + i] for i in range(n1)]
        R = [A[mid + i] for i in range(n2)]
        L.append(1 << 60)
        R.append(1 << 60)
        i = 0
        j = 0
        for k in range(l, r):
            if L[i] <= R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                cnt += n1 - i
                A[k] = R[j]
                j = j + 1

    def merge_sort(A, left, right):
        if len(A) == 1:
            return
        if left+1 < right:
            mid = (left + right) // 2
            merge_sort(A, left, mid)
            merge_sort(A, mid, right)
            merge(A, left, mid, right)

    merge_sort(A, 0, N)

    print(cnt)


if __name__ == '__main__':
    main()

