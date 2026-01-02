def merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    NL = len(L)
    NR = len(R)
    i = 0
    j = 0
    for k in range(left, right):
        if i == NL:
            A[k] = R[j]
            j += 1
        elif j == NR:
            A[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return right - left


def mergesort(A, left, right):
    ans = 0
    if right - left > 1:
        mid = (left + right) // 2
        ans += mergesort(A, left, mid)
        ans += mergesort(A, mid, right)
        ans += merge(A, left, mid, right)
    return ans


def main():
    N, *S = map(int, open(0).read().split())
    ret = mergesort(S, 0, len(S))
    print(' '.join(map(str, S)))
    print(ret)


if __name__ == '__main__':
    main()
