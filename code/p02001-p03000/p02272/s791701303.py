def merge(A, left, mid, right):
    count = 0
    INF = 1000000000000000000000
    n1 = mid - left
    n2 = right - mid

    L = [A[left+i] for i in range(n1)]
    R = [A[mid+i] for i in range(n2)]
    L.append(INF)
    R.append(INF)

    i, j = 0, 0
    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
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


def main():
    global A
    n = int(input())
    A = list(map(int, input().split()))
    count = merge_sort(A, 0, len(A))
    print(" ".join([str(a) for a in A]))
    print(count)

main()

