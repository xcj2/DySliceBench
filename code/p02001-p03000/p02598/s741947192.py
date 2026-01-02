def main():
    from math import ceil

    N, K = map(int, input().split())
    *A, = map(int, input().split())

    def binary_search(*, ok, ng, func):
        for _ in range(60):
            mid = (ok + ng) / 2
            if func(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(mid):
        cnt = 0
        for x in A:
            q, r = divmod(x, mid)
            cnt += q
            if r == 0:
                cnt -= 1
        return cnt <= K

    ma = max(A)
    res = binary_search(ok=ma, ng=0, func=is_ok)

    print(ceil(res))


if __name__ == '__main__':
    main()
