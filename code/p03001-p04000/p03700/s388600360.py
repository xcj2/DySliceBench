def main():
    import sys
    input = sys.stdin.buffer.readline
    N, A, B = (int(i) for i in input().split())
    H = [int(input()) for i in range(N)]

    def is_ok(x):
        need = 0
        cur = [0]*N
        for i, h in enumerate(H):
            cur.append(max(0, h - B*x))
        for i, less in enumerate(cur):
            need += (less+(A-B)-1)//(A-B)
        if need <= x:
            return True
        else:
            return False

    def binary_search_meguru():
        ng = -1
        ok = 10**9 + 1
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
