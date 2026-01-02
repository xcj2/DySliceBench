def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()

    def is_ok(l1, l2, l3):
        if A[l2] < A[l1] + A[l3]:
            return True
        else:
            return False

    def binary_search_meguru(l1, l2):
        ng = l1
        ok = l2
        while abs(ok - ng) > 1:
            mid = ng + (ok - ng) // 2
            if is_ok(l1, l2, mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans = 0
    for l1 in range(N):
        for l2 in range(l1+1, N):
            # l2 を最大辺とする
            ans += l2 - binary_search_meguru(l1, l2)
    print(ans)


if __name__ == '__main__':
    main()
