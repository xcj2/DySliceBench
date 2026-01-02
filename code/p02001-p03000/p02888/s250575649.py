import bisect
def bisect_right_reverse(a, x):
    '''
    reverseにソートされたlist aに対してxを挿入できるidxを返す。
    xが存在する場合には一番右側のidx+1となる。
    '''
    if a[0] < x:
        return 0
    if x <= a[-1]:
        return len(a)
    # 二分探索
    ok = len(a) - 1
    ng = 0
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if a[mid] < x:
            ok = mid
        else:
            ng = mid
    return ok
def bisect_left_reverse(a, x):
    '''
    reverseにソートされたlist aに対してxを挿入できるidxを返す。
    xが存在する場合には一番左側のidxとなる。
    '''
    if a[0] <= x:
        return 0
    if x < a[-1]:
        return len(a)
    # 二分探索
    ok = len(a) - 1
    ng = 0
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if a[mid] <= x:
            ok = mid
        else:
            ng = mid
    return ok
def main2():
    n = int(input())
    l=[int(i) for i in input().split()]
    l.sort(reverse = True)
    res = 0
    for i in range(n-1):
        for j in range(i+1, n-1):
            #index がj以降で　k < c を満たすcで一番小さいc'を探す
            #index(c')-j - 1が三角形の条件を満たす
            nibu = l[j+1:]
            k = max(l[i]-l[j],l[j]-l[i])
            left=bisect_left_reverse(nibu,k)
            res += left
    print(res)

if __name__ == '__main__':
    main2()
