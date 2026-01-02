def main():
    from itertools import accumulate
    N, M, K = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    sA = list(accumulate([0] + A))
    sB = list(accumulate([0] + B))

    def is_ok(t, j):
        if t + sB[j] <= K:
            return True
        else:
            return False

    def binary_search_meguru(t):
        ng = M + 1
        ok = 0
        while abs(ok - ng) > 1:
            mid = ng + (ok - ng) // 2
            if is_ok(t, mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans = 0
    for i in range(N+1):
        # A をi冊読むと決める
        if K < sA[i]:
            break
        v = i + binary_search_meguru(sA[i])
        ans = max(ans, v)
    print(ans)


if __name__ == '__main__':
    main()
