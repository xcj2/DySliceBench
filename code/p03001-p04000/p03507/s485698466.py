def main():
    import sys
    input = sys.stdin.buffer.readline
    N, K = (int(i) for i in input().split())
    WD = [[int(i) for i in input().split()] for j in range(N)]
    ma_w = 0
    ma_d = 0
    for w, d in WD:
        if ma_w < w:
            ma_w = w
        if ma_d < d:
            ma_d = d

    def is_ok(X):
        need = 0
        for i in range(N):
            if WD[i][0] <= X:
                need += ((X - WD[i][0]) // WD[i][1]) + 1
        if need >= K:
            return True
        else:
            return False

    def binary_search_meguru():
        ng = -1
        ok = ma_w + K * ma_d + 1
        while abs(ok - ng) > 1:
            mid = ng + (ok - ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(binary_search_meguru())


if __name__ == '__main__':
    main()
