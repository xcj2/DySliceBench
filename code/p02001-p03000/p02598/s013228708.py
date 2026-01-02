import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    N, K = in_nn()
    A = in_nl()

    def is_ok(x):

        cnt = 0
        for i in range(N):
            q, r = divmod(A[i], x)
            if r == 0:
                q -= 1
            cnt += q

        return cnt <= K

    def bisect(ng, ok):

        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans = bisect(0, 10**9 + 1)
    print(ans)


if __name__ == '__main__':
    main()
