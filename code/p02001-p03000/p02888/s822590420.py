def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    L = [int(i) for i in input().split()]
    L.sort()

    def is_ok(i, j, k):
        if L[j]+L[k] > L[i]:
            return True
        else:
            return False

    def binary_search_meguru(i, j):
        ng = -1
        ok = j
        while abs(ok - ng) > 1:
            mid = ng + (ok - ng) // 2
            if is_ok(i, j, mid):
                ok = mid
            else:
                ng = mid
        return ok
    ans = 0
    for i in range(2, N):
        # i番目を最長辺とする
        for j in range(i):
            k = binary_search_meguru(i, j)
            # print(i, j, k)
            ans += j-k
    print(ans)


if __name__ == '__main__':
    main()
