INF = 10**10


def partition(ary, p, r):
    x = ary[r][1]
    i = p - 1
    for j in range(p, r):
        if ary[j][1] <= x:
            i += 1
            ary[i], ary[j] = ary[j], ary[i]

    ary[i + 1], ary[r] = ary[r], ary[i + 1]

    return i + 1


def quick_sort(ary, p, r):
    if p < r:
        q = partition(ary, p, r)
        quick_sort(ary, p, q - 1)
        quick_sort(ary, q + 1, r)


def merge(ary, left, mid, right):
    lry = ary[left:mid]
    rry = ary[mid:right]
    lry.append(('INF', INF))
    rry.append(('INF', INF))

    i = 0
    j = 0
    for k in range(left, right):
        if lry[i][1] <= rry[j][1]:
            ary[k] = lry[i]
            i += 1
        else:
            ary[k] = rry[j]
            j += 1

    return right - left


def merge_sort(ary, left, right):
    cnt = 0
    if left + 1 < right:
        mid = (left + right) // 2
        cnt += merge_sort(ary, left, mid)
        cnt += merge_sort(ary, mid, right)
        cnt += merge(ary, left, mid, right)

    return cnt


if __name__ == '__main__':
    import sys
    from copy import deepcopy

    n = int(input())
    ary = [(lambda x: (x[0], int(x[1])))(line.strip().split()) for line in sys.stdin]

    qary = deepcopy(ary)
    mary = deepcopy(ary)
    quick_sort(qary, 0, n - 1)
    merge_sort(mary, 0, n)

    if qary == mary:
        print('Stable')
    else:
        print('Not stable')
    [print(*_) for _ in qary]

