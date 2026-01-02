def lower_bound(a, target):
    ng = -1
    ok = len(a)
    while abs(ng-ok) > 1:
        mid = (ng+ok)//2
        if a[mid] >= target:
            ok = mid
        else:
            ng = mid
    return ok


def upper_bound(a, target):
    ng = -1
    ok = len(a)
    while abs(ng-ok) > 1:
        mid = (ng+ok)//2
        if a[mid] > target:
            ok = mid
        else:
            ng = mid
    return ok


def main():
    N = int(input())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    C = sorted(map(int, input().split()))

    ans = 0
    for i in range(N):
        b = B[i]
        ia = lower_bound(A, b)
        ic = upper_bound(C, b)

        ans += (N-ic)*ia
    print(ans)


if __name__ == '__main__':
    main()