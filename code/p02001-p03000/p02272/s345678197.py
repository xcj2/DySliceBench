count = 0


def main():
    input()
    A = [int(x) for x in list(input().split())]
    merge_sort(A, 0, len(A))
    print(*A)
    print(count)


def merge_sort(A, left, right):
    if left+1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


def merge(A, left, mid, right):
    global count
    n1 = mid - left
    n2 = right - mid

    # リストの左側を作成
    L = A[left:mid]

    # リストの右側を作成
    R = A[mid:right]

    # 終端追加
    L.append(float("inf"))
    R.append(float("inf"))

    i = 0
    j = 0
    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


if __name__ == '__main__':
    main()

