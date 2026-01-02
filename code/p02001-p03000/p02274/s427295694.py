def get_num_inversions(A, left, right):
    num_inversions = 0
    if right - left <= 1:
        return num_inversions

    mid = (left+right) // 2
    num_inversions += get_num_inversions(A, left, mid)
    num_inversions += get_num_inversions(A, mid, right)
    num_inversions = merge(A, left, mid, right, num_inversions)

    return num_inversions


def merge(A, left, mid, right, num_inversions):
    n1 = mid - left
    n2 = right - mid
    L = [A[left+i] for i in range(n1)]
    R = [A[mid+i] for i in range(n2)]

    L.append(1e10)
    R.append(1e10)

    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            num_inversions += len(L) - i - 1 # -1はappendした1e10の分

    return num_inversions


def main():
    n = int(input())
    A = list(map(int, input().split()))
    print(get_num_inversions(A, 0, n))


if __name__ == '__main__':
    main()
