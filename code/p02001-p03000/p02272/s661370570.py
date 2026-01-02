def merge(A, left, mid, right, cnt):
    n1 = mid - left
    n2 = right - mid
    L = [A[left+i] for i in range(n1)]
    R = [A[mid+i] for i in range(n2)]

    L.append(1e10)
    R.append(1e10)

    i = 0 
    j = 0
    c = 0
    for k in range(left, right):
        c += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1 
        else:
            A[k] = R[j]
            j += 1

    else:
        cnt.append(c)


def mergeSort(A, left, right, cnt):
    if left+1 < right:
        mid = (left+right) // 2
        mergeSort(A, left, mid, cnt)
        mergeSort(A, mid, right, cnt)
        merge(A, left, mid, right, cnt)


def main():
    cnt = []
    _ = int(input())
    S = list(map(int, input().split()))
    mergeSort(S, 0, len(S), cnt)
    print(*S)
    print(sum(cnt))


if __name__ == "__main__":
    main()

