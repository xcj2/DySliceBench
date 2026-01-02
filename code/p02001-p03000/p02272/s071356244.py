SENTINEL = 1e+9
t = 0


def Merge(A, left, mid, right):
    global t
    n1 = mid - left
    n2 = right - mid
    L, R = A[left:left+n1], A[mid:mid+n2]
    L.append(SENTINEL)
    R.append(SENTINEL)
    i, j = 0, 0
    for k in range(left, right):
        t += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def Merge_Sort(A, left, right):
    if left+1 < right:
        mid = (left + right) // 2
        Merge_Sort(A, left, mid)
        Merge_Sort(A, mid, right)
        Merge(A, left, mid, right)


def main():
    global t
    input()
    A = [int(i) for i in input().split()]
    Merge_Sort(A, 0, len(A))
    print(*A)
    print(t)


if __name__ == '__main__':
    main()

