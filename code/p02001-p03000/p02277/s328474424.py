def merge(A, left, mid, right):
    count = 0
    INF = 1000000000000000000000
    n1 = mid - left
    n2 = right - mid

    L = [A[left+i] for i in range(n1)]
    R = [A[mid+i] for i in range(n2)]
    L.append((INF, INF))
    R.append((INF, INF))

    i, j = 0, 0
    for k in range(left, right):
        count += 1
        # print(L[i][1], R[j][1])
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return count


def merge_sort(A, left, right):
    if left+1 < right:
        mid = (left + right) // 2
        count_left = merge_sort(A, left, mid)
        count_right = merge_sort(A, mid, right)
        count = merge(A, left, mid, right)
        return count + count_right + count_left
    return 0


def partition(A, p, r):
    x = A[r][1]
    i = p-1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def main():
    import copy
    n = int(input())
    A = []
    for _ in range(n):
        a, b = input().split()
        A.append((a, int(b)))

    B = copy.deepcopy(A)

    merge_sort(B, 0, len(B))
    quick_sort(A, 0, n-1)

    # print(A, B)

    if A == B:
        print("Stable")
    else:
        print("Not stable")

    for a in A:
        print(f"{a[0]} {a[1]}")

if __name__ == "__main__":
    main()
